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

      const WEBHOOK_URL = 'https://www.nida-os.com/api/inbound-webhook?workspace_id=4a9a195e-fc77-4b3a-9304-fc940d575e13';
      let ok = false;

      try {
        const resp = await fetch(WEBHOOK_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer inb_64e8411f2c432dbdbe1d2f334f7744b0bb9fcd26' },
          body: JSON.stringify(payload)
        });
        ok = resp.ok;
        if (!ok) console.error('Webhook returned HTTP', resp.status, await resp.text());
      } catch (err) {
        console.error('Webhook fetch failed:', err);
      }

      if (ok) {
        btn.textContent = '\u2713 Quote Requested!';
        btn.style.background = 'var(--green)';
      } else {
        btn.textContent = 'Error — try calling';
        btn.style.background = '#b00020';
      }
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

      const WEBHOOK_URL = 'https://www.nida-os.com/api/inbound-webhook?workspace_id=4a9a195e-fc77-4b3a-9304-fc940d575e13';
      let ok = false;

      try {
        const resp = await fetch(WEBHOOK_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer inb_64e8411f2c432dbdbe1d2f334f7744b0bb9fcd26' },
          body: JSON.stringify(payload)
        });
        ok = resp.ok;
        if (!ok) console.error('Webhook returned HTTP', resp.status, await resp.text());
      } catch (err) {
        console.error('Webhook fetch failed:', err);
      }

      if (ok) {
        modalForm.style.display = 'none';
        if (modalSuccess) modalSuccess.style.display = 'block';
      } else {
        alert('Something went wrong sending your quote. Please call (804) 848-9575.');
      }
    });
  }

  /* ---- Contact Page Form ---- */
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const btn = contactForm.querySelector('button[type="submit"]');
      const origText = btn.textContent;
      btn.textContent = 'Sending...';
      btn.disabled = true;

      const data = new FormData(contactForm);
      const payload = Object.fromEntries(data.entries());
      payload.source = window.location.pathname;
      payload.timestamp = new Date().toISOString();

      const WEBHOOK_URL = 'https://www.nida-os.com/api/inbound-webhook?workspace_id=4a9a195e-fc77-4b3a-9304-fc940d575e13';
      let ok = false;

      try {
        const resp = await fetch(WEBHOOK_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer inb_64e8411f2c432dbdbe1d2f334f7744b0bb9fcd26' },
          body: JSON.stringify(payload)
        });
        ok = resp.ok;
        if (!ok) console.error('Webhook returned HTTP', resp.status, await resp.text());
      } catch (err) {
        console.error('Webhook fetch failed:', err);
      }

      if (ok) {
        btn.textContent = '\u2713 Message Sent!';
        btn.style.background = 'var(--green)';
      } else {
        btn.textContent = 'Error — try calling';
        btn.style.background = '#b00020';
      }
      setTimeout(() => {
        contactForm.reset();
        btn.textContent = origText;
        btn.disabled = false;
        btn.style.background = '';
      }, 3000);
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



  /* ═══════════════════════════════════════════════════════════════
     Nida Chatbot Widget — Dre Home Services
     ═══════════════════════════════════════════════════════════════ */
  (function() {
    const CHATBOT_ID = '9f7872ba-5d3f-40e7-a511-0a3d572e1330';
    const EMBED_URL = 'https://www.nida-os.com/embed/chatbot/' + CHATBOT_ID;

    const launcher = document.createElement('div');
    launcher.id = 'nida-chatbot-launcher';
    launcher.setAttribute('aria-label', 'Open chat');
    launcher.innerHTML = '\
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\
        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>\
      </svg>';
    launcher.style.cssText = 'position:fixed;bottom:24px;right:24px;width:64px;height:64px;background:#D06000;color:white;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;box-shadow:0 4px 16px rgba(208,96,0,0.4);z-index:9999;transition:transform 0.2s;';

    const panel = document.createElement('iframe');
    panel.id = 'nida-chatbot-panel';
    panel.src = EMBED_URL;
    panel.title = 'Dre Home Services Chat';
    panel.setAttribute('allow', 'clipboard-write');
    panel.style.cssText = 'position:fixed;bottom:100px;right:24px;width:408px;height:640px;max-height:calc(100vh - 120px);border:none;border-radius:28px;box-shadow:0 8px 32px rgba(0,0,0,0.3);z-index:9998;display:none;background:white;';

    let isOpen = false;
    launcher.addEventListener('click', function() {
      isOpen = !isOpen;
      panel.style.display = isOpen ? 'block' : 'none';
      launcher.style.transform = isOpen ? 'scale(0.9)' : 'scale(1)';
    });

    document.body.appendChild(panel);
    document.body.appendChild(launcher);
  })();

})();
