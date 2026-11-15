/* Minimal static ELF launcher for Ren'Py Linux distributions.
 * Ensures X11 SDL backend when DISPLAY is present (for native GTK3 menu bar),
 * then execs lib/py3-linux-x86_64/NaishoNoMahou relative to this binary's directory.
 */
#define _POSIX_C_SOURCE 200809L
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char **argv) {
    char exe_path[PATH_MAX];
    ssize_t n = readlink("/proc/self/exe", exe_path, sizeof(exe_path) - 1);
    if (n <= 0 || n >= (ssize_t)sizeof(exe_path)) {
        fprintf(stderr, "Failed to resolve executable path via /proc/self/exe\n");
        return 127;
    }
    exe_path[n] = '\0';

    char *slash = strrchr(exe_path, '/');
    if (!slash) {
        fprintf(stderr, "Invalid executable path: %s\n", exe_path);
        return 127;
    }
    *slash = '\0';

    const char *display = getenv("DISPLAY");
    const char *sdl_vd = getenv("SDL_VIDEODRIVER");
    const char *sdl_vd3 = getenv("SDL_VIDEO_DRIVER");
    if (display && display[0] != '\0' && (!sdl_vd || sdl_vd[0] == '\0') && (!sdl_vd3 || sdl_vd3[0] == '\0')) {
        setenv("SDL_VIDEODRIVER", "x11", 0);
    }

    char target[PATH_MAX];
    int written = snprintf(target, sizeof(target), "%s/lib/py3-linux-x86_64/NaishoNoMahou", exe_path);
    if (written < 0 || (size_t)written >= sizeof(target)) {
        fprintf(stderr, "Target launcher path too long\n");
        return 127;
    }

    if (access(target, X_OK) != 0) {
        written = snprintf(target, sizeof(target), "%s/NaishoNoMahou.sh", exe_path);
        if (written < 0 || (size_t)written >= sizeof(target)) {
            fprintf(stderr, "Fallback script path too long\n");
            return 127;
        }
    }

    char **new_argv = (char **)calloc((size_t)argc + 1, sizeof(char *));
    if (!new_argv) {
        return 127;
    }
    new_argv[0] = target;
    for (int i = 1; i < argc; i++) {
        new_argv[i] = argv[i];
    }
    new_argv[argc] = NULL;

    execv(target, new_argv);
    perror("execv");
    free(new_argv);
    return 127;
}
