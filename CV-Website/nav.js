document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.getElementById('menuToggle');
  var leftContent = document.querySelector('.left-content');
  var nav = document.querySelector('.nav');

  if (!toggle || !leftContent || !nav) return;

  toggle.addEventListener('click', function () {
    var isOpen = leftContent.classList.toggle('nav-open');
    toggle.classList.toggle('active', isOpen);
    toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  });

  // Close the menu after tapping a nav link (mobile only)
  nav.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      leftContent.classList.remove('nav-open');
      toggle.classList.remove('active');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });
});