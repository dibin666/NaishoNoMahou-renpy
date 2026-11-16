// Official Toei rollover helpers + Bilingual (简体中文 / 日本語) Live Switcher + Lightbox

(function () {
  var STORAGE_KEY = "doremi_lang";
  var currentLang = "zh";
  try {
    var urlLang = new URLSearchParams(window.location.search).get("lang");
    if (urlLang === "zh" || urlLang === "jp") {
      currentLang = urlLang;
    } else {
      var saved = localStorage.getItem(STORAGE_KEY);
      if (saved === "zh" || saved === "jp") currentLang = saved;
    }
  } catch (_) {}

  window.getDoremiLang = function () {
    return currentLang;
  };

  function getAttrForLang(el, base, lang) {
    return el.getAttribute("data-" + base + "-" + lang);
  }

  function preloadSet(lang) {
    var imgs = document.querySelectorAll("img[data-over-" + lang + "]");
    imgs.forEach(function (img) {
      var u = img.getAttribute("data-over-" + lang);
      if (u) {
        var pre = new Image();
        pre.src = u;
      }
    });
  }

  function applyLanguage(lang) {
    currentLang = (lang === "jp") ? "jp" : "zh";
    try { localStorage.setItem(STORAGE_KEY, currentLang); } catch (_) {}
    document.documentElement.lang = (currentLang === "jp") ? "ja" : "zh-CN";

    if (document.body) {
      var pageTitle = document.body.getAttribute("data-title-" + currentLang);
      if (pageTitle) document.title = pageTitle;
    }

    // Update switcher buttons
    document.querySelectorAll(".lang-btn[data-set-lang]").forEach(function (btn) {
      btn.classList.toggle("active", btn.getAttribute("data-set-lang") === currentLang);
    });

    // Update localized images
    document.querySelectorAll("img[data-zh][data-jp]").forEach(function (img) {
      var isTransformed = img.getAttribute("data-transformed") === "1";
      var tSrc = img.getAttribute("data-transform");
      if (isTransformed && tSrc) {
        img.src = tSrc;
      } else {
        img.src = img.getAttribute("data-" + currentLang);
      }
      var altVal = img.getAttribute("data-alt-" + currentLang);
      if (altVal) img.alt = altVal;
    });

    // Update localized text/HTML elements
    document.querySelectorAll("[data-zh][data-jp]:not(img)").forEach(function (el) {
      var val = el.getAttribute("data-" + currentLang);
      if (val === null) return;
      if (el.getAttribute("data-html") === "1") {
        el.innerHTML = val;
      } else {
        el.textContent = val;
      }
    });

    // Update localized title tooltips
    document.querySelectorAll("[data-title-zh][data-title-jp]").forEach(function (el) {
      if (el === document.body) return;
      el.title = el.getAttribute("data-title-" + currentLang);
    });

    preloadSet(currentLang);

    if (typeof window.onDoremiLanguageChange === "function") {
      window.onDoremiLanguageChange(currentLang);
    }
  }

  window.setDoremiLang = applyLanguage;

  // Bind hover swaps cleanly for bilingual images
  function bindBilingualHovers() {
    document.querySelectorAll("img[data-over-zh], img[data-over-jp]").forEach(function (img) {
      var target = img.closest("a") || img;
      target.addEventListener("mouseenter", function () {
        var over = getAttrForLang(img, "over", currentLang);
        if (over) img.src = over;
      });
      target.addEventListener("mouseleave", function () {
        var isTransformed = img.getAttribute("data-transformed") === "1";
        var tSrc = img.getAttribute("data-transform");
        if (isTransformed && tSrc) {
          img.src = tSrc;
        } else {
          var norm = img.getAttribute("data-" + currentLang);
          if (norm) img.src = norm;
        }
      });
    });
  }

  // Character transformation toggle (mirrors official caracter.html)
  window.toggleCharacterTransform = function () {
    var el = document.getElementById("majoImg");
    if (!el) return;
    var isTransformed = el.getAttribute("data-transformed") === "1";
    var tSrc = el.getAttribute("data-transform");
    if (!isTransformed && tSrc) {
      el.setAttribute("data-transformed", "1");
      el.src = tSrc;
    } else {
      el.setAttribute("data-transformed", "0");
      el.src = el.getAttribute("data-" + currentLang);
    }
  };

  // Shared Lightbox for Screenshots / Oyajide Photo Gallery
  window.initDoremiLightbox = function (shots) {
    var lb = document.getElementById("lightbox");
    if (!lb) return;
    var lbImg = document.getElementById("lbImg");
    var lbCap = document.getElementById("lbCaption");
    var idx = 0;

    function openLb(i) {
      idx = (i + shots.length) % shots.length;
      var s = shots[idx];
      var cap = (currentLang === "jp" && s.caption_jp) ? s.caption_jp : s.caption;
      lbImg.src = s.src;
      lbImg.alt = cap;
      lbCap.textContent = cap;
      lb.classList.add("open");
    }
    function closeLb() {
      lb.classList.remove("open");
    }
    window.openDoremiLightbox = openLb;

    document.querySelectorAll("[data-lb-index]").forEach(function (el) {
      el.addEventListener("click", function () {
        openLb(Number(el.getAttribute("data-lb-index")));
      });
    });

    var btnClose = document.getElementById("lbClose");
    var btnPrev = document.getElementById("lbPrev");
    var btnNext = document.getElementById("lbNext");
    if (btnClose) btnClose.addEventListener("click", closeLb);
    if (btnPrev) btnPrev.addEventListener("click", function () { openLb(idx - 1); });
    if (btnNext) btnNext.addEventListener("click", function () { openLb(idx + 1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) closeLb(); });
    document.addEventListener("keydown", function (e) {
      if (!lb.classList.contains("open")) return;
      if (e.key === "Escape") closeLb();
      if (e.key === "ArrowLeft") openLb(idx - 1);
      if (e.key === "ArrowRight") openLb(idx + 1);
    });
  };

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".lang-btn[data-set-lang]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        applyLanguage(btn.getAttribute("data-set-lang"));
      });
    });
    bindBilingualHovers();
    applyLanguage(currentLang);
  });
})();
