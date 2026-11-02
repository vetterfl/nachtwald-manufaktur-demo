// Nachtwald Manufaktur – Demo Shop: kleine UI-Interaktionen (kein echter Shop-Backend-Code).
(function () {
  "use strict";

  // Mobiles Menü
  var toggle = document.getElementById("navToggle");
  var nav = document.getElementById("siteNav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  // FAQ Akkordeon
  document.querySelectorAll(".faq-item__question").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var item = btn.closest(".faq-item");
      var isOpen = item.classList.contains("is-open");
      document.querySelectorAll(".faq-item.is-open").forEach(function (open) {
        if (open !== item) {
          open.classList.remove("is-open");
          open.querySelector(".faq-item__question").setAttribute("aria-expanded", "false");
        }
      });
      item.classList.toggle("is-open", !isOpen);
      btn.setAttribute("aria-expanded", (!isOpen).toString());
    });
  });

  // Demo-Warenkorb: rein visuelles Feedback, keine echte Funktion.
  var toast = document.getElementById("cartToast");
  var toastTimer = null;
  document.querySelectorAll("[data-demo-cart]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var name = btn.getAttribute("data-product") || "Produkt";
      if (toast) {
        toast.textContent = "„" + name + "“ zum Demo-Warenkorb hinzugefügt. Dies ist keine echte Bestellung.";
        toast.hidden = false;
        clearTimeout(toastTimer);
        toastTimer = setTimeout(function () {
          toast.hidden = true;
        }, 3200);
      }
    });
  });

  // Demo-Kontaktformular: verhindert echtes Absenden.
  document.querySelectorAll("[data-demo-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var btn = form.querySelector("button[type=submit]");
      if (btn) {
        var original = btn.textContent;
        btn.textContent = "Demo – nicht wirklich gesendet";
        setTimeout(function () {
          btn.textContent = original;
        }, 2600);
      }
    });
  });
})();
