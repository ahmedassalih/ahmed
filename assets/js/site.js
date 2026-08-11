/* Mobile navigation overlay. Progressive enhancement: without JavaScript the
   navigation stays in the document flow and every link remains reachable. */
(function () {
  'use strict';

  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (!toggle || !nav) return;

  var root = document.documentElement;
  var lastFocus = null;

  function isOpen() {
    return toggle.getAttribute('aria-expanded') === 'true';
  }

  function setOpen(open) {
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    nav.classList.toggle('is-open', open);
    // Lock the page behind the overlay without losing scroll position.
    root.classList.toggle('nav-open', open);
    if (open) {
      lastFocus = document.activeElement;
      var first = nav.querySelector('a');
      if (first) first.focus();
    } else if (lastFocus && typeof lastFocus.focus === 'function') {
      lastFocus.focus();
    }
  }

  toggle.addEventListener('click', function () {
    setOpen(!isOpen());
  });

  // Following a link should close the overlay.
  nav.addEventListener('click', function (event) {
    if (event.target.closest('a')) setOpen(false);
  });

  document.addEventListener('keydown', function (event) {
    if (event.key !== 'Escape' || !isOpen()) return;
    setOpen(false);
    toggle.focus();
  });

  // Keep focus inside the overlay while it is open.
  nav.addEventListener('keydown', function (event) {
    if (event.key !== 'Tab' || !isOpen()) return;
    var items = nav.querySelectorAll('a[href]');
    if (!items.length) return;
    var first = items[0];
    var last = items[items.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      toggle.focus();
    }
  });

  // A resize past the breakpoint returns to the desktop navigation.
  var wide = window.matchMedia('(min-width: 901px)');
  var onChange = function (event) { if (event.matches && isOpen()) setOpen(false); };
  if (wide.addEventListener) wide.addEventListener('change', onChange);
  else if (wide.addListener) wide.addListener(onChange);
})();
