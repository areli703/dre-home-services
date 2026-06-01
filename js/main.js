/* ============================================
   Dre Home Services — Evidence-Based Interactions v4
   ============================================ */

(function() {
  'use strict';

  /* ---- Scroll Reveals ---- */
  const srObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) entry.target.classList.add('visible');
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -60px 0px' });
  document.querySelectorAll('.sr').forEach(el => srObserver.observe(el));

  /* ---- Nav Scroll Effect ---- */
  const nav = document.querySelector('nav');
  if (nav) {
    window.addEventListener('scroll', () => {
      nav.classList.toggle('scrolled', window.scrollY > 20);
    }, { passive: true });
  }

  /* ---- Mobile Menu ---- */
  const menuBtn = document.querySelector('.mobile-menu-btn');
  const mobileNav = document.querySelector('.mobile-nav');
  if (menuBtn && mobileNav) {
    menuBtn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      mobileNav.classList.toggle('open');
      menuBtn.innerHTML = mobileNav.classList.contains('open') ? '&times;' : '&#9776;';
    });
    mobileNav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileNav.classList.remove('open');
        menuBtn.innerHTML = '&#9776;';
      });
    });
    document.addEventListener('click', (e) => {
      if (!mobileNav.contains(e.target) && !menuBtn.contains(e.target)) {
        mobileNav.classList.remove('open');
        menuBtn.innerHTML = '&#9776;';
      }
    });
  }

  /* ---- Hero Inline Form ---- */
  const heroForm = document.getElementById('hero-form');
  if (heroForm) {
    heroForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const btn = heroForm.querySelector('button[type="submit"]');
      const origText = btn.textContent;
      btn.textContent = 'Sending...';
      btn.disabled = true;

      const data = new FormData(heroForm);
      const payload = Object.fromEntries(data.entries());
      payload.source = window.location.pathname;
      payload.timestamp = new Date().toISOString();

      // Replace with your actual Nida webhook URL
      const WEBHOOK_URL = 'https://your-nida-webhook-url-here';

      try {
        await fetch(WEBHOOK_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
      } catch (err) {
        console.log('Webhook not configured — payload:', payload);
      }

      btn.textContent = '✓ Quote Requested!';
      btn.style.background = 'var(--green)';
      setTimeout(() => {
        heroForm.reset();
        btn.textContent = origText;
        btn.disabled = false;
        btn.style.background = '';
      }, 3000);
    });
  }

  /* ---- Modal (for subpages) ---- */
  const modal = document.getElementById('quote-modal');
  const modalForm = document.getElementById('quote-form');
  const modalSuccess = document.getElementById('modal-success');

  function openModal() {
    if (!modal) return;
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
    if (modalSuccess) modalSuccess.style.display = 'none';
    if (modalForm) modalForm.style.display = 'block';
  }
  function closeModal() {
    if (!modal) return;
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  document.querySelectorAll('[data-open-modal]').forEach(btn => {
    btn.addEventListener('click', openModal);
  });
  document.querySelectorAll('.modal-close, .modal-overlay').forEach(el => {
    el.addEventListener('click', (e) => {
      if (e.target === el) closeModal();
    });
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal && modal.classList.contains('active')) closeModal();
  });

  if (modalForm) {
    modalForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const data = new FormData(modalForm);
      const payload = Object.fromEntries(data.entries());
      payload.source = window.location.pathname;
      payload.timestamp = new Date().toISOString();

      const WEBHOOK_URL = 'https://your-nida-webhook-url-here';
      try {
        await fetch(WEBHOOK_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
      } catch (err) {
        console.log('Webhook not configured — payload:', payload);
      }

      modalForm.style.display = 'none';
      if (modalSuccess) modalSuccess.style.display = 'block';
    });
  }

  /* ---- FAQ Accordion ---- */
  document.querySelectorAll('.faq-question').forEach(q => {
    q.addEventListener('click', () => {
      const item = q.parentElement;
      const wasOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
      if (!wasOpen) item.classList.add('open');
    });
  });

  /* ---- Smooth Scroll ---- */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

})();
