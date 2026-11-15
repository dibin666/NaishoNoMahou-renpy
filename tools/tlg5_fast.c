#include <stdint.h>
#include <stdlib.h>
#include <string.h>

/*
 * Fast KiriKiri TLG5.0 lossless decoder returning tightly packed RGBA pixels.
 * Output buffer must be allocated by caller with size (width * height * 4) bytes,
 * or call tlg5_get_info first to obtain width, height, and channel count.
 */

static void lzss_decompress(
    uint8_t *outbuf,
    size_t out_limit,
    const uint8_t *inbuf,
    size_t inbufsize,
    uint8_t *text,
    int *r_ptr
) {
    int r = *r_ptr;
    unsigned int flags = 0;
    const uint8_t *in = inbuf;
    const uint8_t *in_end = inbuf + inbufsize;
    uint8_t *out = outbuf;
    uint8_t *out_end = outbuf + out_limit;

    while (in < in_end && out < out_end) {
        flags >>= 1;
        if ((flags & 0x100) == 0) {
            if (in >= in_end) break;
            flags = (unsigned int)(*in++) | 0xff00u;
        }
        if (flags & 1) {
            if (in + 1 >= in_end) break;
            int mpos = (int)in[0] | (((int)in[1] & 0x0f) << 8);
            int mlen = ((int)in[1] & 0xf0) >> 4;
            in += 2;
            mlen += 3;
            if (mlen == 18) {
                if (in >= in_end) break;
                mlen += (int)(*in++);
            }
            while (mlen-- > 0 && out < out_end) {
                uint8_t v = text[mpos++];
                *out++ = v;
                text[r++] = v;
                mpos &= 4095;
                r &= 4095;
            }
        } else {
            if (in >= in_end) break;
            uint8_t v = *in++;
            *out++ = v;
            text[r++] = v;
            r &= 4095;
        }
    }
    *r_ptr = r;
}

static uint32_t read_u32_le(const uint8_t *p) {
    return (uint32_t)p[0] | ((uint32_t)p[1] << 8) | ((uint32_t)p[2] << 16) | ((uint32_t)p[3] << 24);
}

/* Returns 0 on success, non-zero on invalid header or allocation failure. */
int tlg5_get_info(const uint8_t *data, size_t size, int *out_w, int *out_h, int *out_colors, size_t *out_data_offset) {
    if (!data || size < 24) return -1;

    size_t offset = 0;
    /* Handle optional TLG0.0 sds wrapper */
    if (size >= 15 && memcmp(data, "TLG0.0\x00sds\x1a\x00", 11) == 0) {
        uint32_t raw_len = read_u32_le(data + 11);
        offset = 15;
        if (offset + raw_len > size || raw_len < 24) return -2;
    }

    if (memcmp(data + offset, "TLG5.0\x00raw\x1a", 11) != 0) {
        return -3;
    }

    int colors = (int)data[offset + 11];
    if (colors != 1 && colors != 3 && colors != 4) return -4;

    uint32_t w = read_u32_le(data + offset + 12);
    uint32_t h = read_u32_le(data + offset + 16);
    if (w == 0 || h == 0 || w > 16384 || h > 16384) return -5;

    if (out_w) *out_w = (int)w;
    if (out_h) *out_h = (int)h;
    if (out_colors) *out_colors = colors;
    if (out_data_offset) *out_data_offset = offset;
    return 0;
}

int tlg5_decode_rgba(const uint8_t *data, size_t size, uint8_t *out_rgba) {
    int width = 0, height = 0, colors = 0;
    size_t base_off = 0;
    int rc = tlg5_get_info(data, size, &width, &height, &colors, &base_off);
    if (rc != 0 || !out_rgba) return rc != 0 ? rc : -1;

    const uint8_t *p = data + base_off + 12;
    const uint8_t *end = data + size;

    p += 8; /* skip width, height */
    if (p + 4 > end) return -6;
    uint32_t blockheight = read_u32_le(p);
    p += 4;
    if (blockheight == 0) return -7;

    uint32_t blockcount = ((uint32_t)height - 1u) / blockheight + 1u;
    if (p + (size_t)blockcount * 4u > end) return -8;
    p += (size_t)blockcount * 4u; /* skip block sizes array */

    size_t max_chan_bytes = (size_t)width * (size_t)blockheight;
    uint8_t *ch_buf[4] = {NULL, NULL, NULL, NULL};
    for (int c = 0; c < colors; c++) {
        ch_buf[c] = (uint8_t *)malloc(max_chan_bytes);
        if (!ch_buf[c]) {
            for (int j = 0; j < c; j++) free(ch_buf[j]);
            return -9;
        }
    }

    uint8_t *prevline = (uint8_t *)calloc((size_t)width * 4u, 1);
    if (!prevline) {
        for (int c = 0; c < colors; c++) free(ch_buf[c]);
        return -10;
    }

    uint8_t text[4096];
    memset(text, 0, sizeof(text));
    int r = 0;

    int decode_err = 0;
    for (int y_blk = 0; y_blk < height; y_blk += (int)blockheight) {
        int cur_bh = (y_blk + (int)blockheight <= height) ? (int)blockheight : (height - y_blk);
        size_t blk_pixels = (size_t)width * (size_t)cur_bh;

        for (int c = 0; c < colors; c++) {
            if (p + 5 > end) {
                decode_err = -11;
                break;
            }
            uint8_t mark = *p++;
            uint32_t bsize = read_u32_le(p);
            p += 4;
            if (p + bsize > end) {
                decode_err = -12;
                break;
            }
            if (mark == 0) {
                lzss_decompress(ch_buf[c], blk_pixels, p, bsize, text, &r);
            } else {
                size_t to_copy = bsize < blk_pixels ? bsize : blk_pixels;
                memcpy(ch_buf[c], p, to_copy);
                if (to_copy < blk_pixels) {
                    memset(ch_buf[c] + to_copy, 0, blk_pixels - to_copy);
                }
            }
            p += bsize;
        }
        if (decode_err) break;

        for (int y = 0; y < cur_bh; y++) {
            size_t row_off = (size_t)y * (size_t)width;
            uint8_t *dst = out_rgba + ((size_t)(y_blk + y) * (size_t)width * 4u);
            uint8_t pr = 0, pg = 0, pb = 0, pa = 0;

            if (colors == 4) {
                const uint8_t *b0 = ch_buf[0] + row_off;
                const uint8_t *b1 = ch_buf[1] + row_off;
                const uint8_t *b2 = ch_buf[2] + row_off;
                const uint8_t *b3 = ch_buf[3] + row_off;
                for (int x = 0; x < width; x++) {
                    uint8_t g = b1[x];
                    uint8_t b = (uint8_t)(b0[x] + g);
                    uint8_t r_val = (uint8_t)(b2[x] + g);
                    uint8_t a = b3[x];
                    pb = (uint8_t)(pb + b);
                    pg = (uint8_t)(pg + g);
                    pr = (uint8_t)(pr + r_val);
                    pa = (uint8_t)(pa + a);
                    uint8_t out_r = (uint8_t)(prevline[x * 4 + 0] + pr);
                    uint8_t out_g = (uint8_t)(prevline[x * 4 + 1] + pg);
                    uint8_t out_b = (uint8_t)(prevline[x * 4 + 2] + pb);
                    uint8_t out_a = (uint8_t)(prevline[x * 4 + 3] + pa);
                    dst[x * 4 + 0] = prevline[x * 4 + 0] = out_r;
                    dst[x * 4 + 1] = prevline[x * 4 + 1] = out_g;
                    dst[x * 4 + 2] = prevline[x * 4 + 2] = out_b;
                    dst[x * 4 + 3] = prevline[x * 4 + 3] = out_a;
                }
            } else if (colors == 3) {
                const uint8_t *b0 = ch_buf[0] + row_off;
                const uint8_t *b1 = ch_buf[1] + row_off;
                const uint8_t *b2 = ch_buf[2] + row_off;
                for (int x = 0; x < width; x++) {
                    uint8_t g = b1[x];
                    uint8_t b = (uint8_t)(b0[x] + g);
                    uint8_t r_val = (uint8_t)(b2[x] + g);
                    pb = (uint8_t)(pb + b);
                    pg = (uint8_t)(pg + g);
                    pr = (uint8_t)(pr + r_val);
                    uint8_t out_r = (uint8_t)(prevline[x * 4 + 0] + pr);
                    uint8_t out_g = (uint8_t)(prevline[x * 4 + 1] + pg);
                    uint8_t out_b = (uint8_t)(prevline[x * 4 + 2] + pb);
                    dst[x * 4 + 0] = prevline[x * 4 + 0] = out_r;
                    dst[x * 4 + 1] = prevline[x * 4 + 1] = out_g;
                    dst[x * 4 + 2] = prevline[x * 4 + 2] = out_b;
                    dst[x * 4 + 3] = 255;
                    prevline[x * 4 + 3] = 255;
                }
            } else { /* colors == 1 */
                const uint8_t *b0 = ch_buf[0] + row_off;
                for (int x = 0; x < width; x++) {
                    pg = (uint8_t)(pg + b0[x]);
                    uint8_t out_v = (uint8_t)(prevline[x * 4 + 0] + pg);
                    dst[x * 4 + 0] = prevline[x * 4 + 0] = out_v;
                    dst[x * 4 + 1] = prevline[x * 4 + 1] = out_v;
                    dst[x * 4 + 2] = prevline[x * 4 + 2] = out_v;
                    dst[x * 4 + 3] = 255;
                    prevline[x * 4 + 3] = 255;
                }
            }
        }
    }

    free(prevline);
    for (int c = 0; c < colors; c++) free(ch_buf[c]);
    return decode_err;
}
