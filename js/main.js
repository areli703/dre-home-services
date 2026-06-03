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
      const WEBHOOK_URL = 'https://www.nida-os.com/api/inbound-webhook?workspace_id=4a9a195e-fc77-4b3a-9304-fc940d575e13';

      try {
        await fetch(WEBHOOK_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'X-Nida-Secret': 'inb_64e8411f2c432dbdbe1d2f334f7744b0bb9fcd26' },
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



  /* ═══════════════════════════════════════════════════════════════
     Chatbot Widget — Dre Home Services
     ═══════════════════════════════════════════════════════════════ */
  (function() {
    const WEBHOOK_URL = 'https://www.nida-os.com/api/inbound-webhook?workspace_id=4a9a195e-fc77-4b3a-9304-fc940d575e13';
    const NIDA_SECRET = 'inb_64e8411f2c432dbdbe1d2f334f7744b0bb9fcd26';

    // Create widget HTML
    const widgetHTML = `
    <div class="chat-widget" id="chat-widget" aria-label="Open chat">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
    </div>
    <div class="chat-panel" id="chat-panel">
      <div class="chat-header">
        <div class="chat-header-info">
          <div class="chat-avatar">D</div>
          <div>
            <div class="chat-title">Dre Home Services</div>
            <div class="chat-status">
              <span class="chat-status-dot"></span>Online — replies instantly
            </div>
          </div>
        </div>
        <button class="chat-close" id="chat-close" aria-label="Close chat">&times;</button>
      </div>
      <div class="chat-messages" id="chat-messages">
        <div class="chat-message bot">
          <div class="chat-bubble">Hi! I'm Dre's virtual assistant. How can I help you with your roofing, plumbing, or electrical project today?</div>
          <div class="chat-time">Just now</div>
        </div>
      </div>
      <div class="chat-input-area">
        <input type="text" id="chat-input" placeholder="Type your message..." autocomplete="off">
        <button id="chat-send" aria-label="Send message">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg>
        </button>
      </div>
      <div class="chat-footer">Powered by Dre Home Services</div>
    </div>`;

    const div = document.createElement('div');
    div.innerHTML = widgetHTML;
    document.body.appendChild(div);

    const widget = document.getElementById('chat-widget');
    const panel = document.getElementById('chat-panel');
    const closeBtn = document.getElementById('chat-close');
    const input = document.getElementById('chat-input');
    const sendBtn = document.getElementById('chat-send');
    const messages = document.getElementById('chat-messages');

    let isOpen = false;
    let capturedInfo = { name: '', email: '', phone: '' };
    let step = 'chatting'; // chatting -> ask_name -> ask_email -> ask_phone -> done

    function toggle() {
      isOpen = !isOpen;
      panel.classList.toggle('open', isOpen);
      widget.classList.toggle('open', isOpen);
      if (isOpen) input.focus();
    }

    widget.addEventListener('click', toggle);
    closeBtn.addEventListener('click', toggle);

    function addMessage(text, isBot) {
      const msg = document.createElement('div');
      msg.className = 'chat-message ' + (isBot ? 'bot' : 'user');
      msg.innerHTML = `<div class="chat-bubble">${text}</div><div class="chat-time">Just now</div>`;
      messages.appendChild(msg);
      messages.scrollTop = messages.scrollHeight;
    }

    function botReply(userText) {
      const lower = userText.toLowerCase();
      let reply = '';

      if (step === 'ask_name') {
        capturedInfo.name = userText;
        step = 'ask_email';
        reply = "Thanks, " + userText + "! What's your email address so we can send you a confirmation?";
      } else if (step === 'ask_email') {
        capturedInfo.email = userText;
        step = 'ask_phone';
        reply = "Perfect. And your phone number so Andre can call you back within 15 minutes?";
      } else if (step === 'ask_phone') {
        capturedInfo.phone = userText;
        step = 'done';
        reply = "Great! We've got your info. Andre will call you at " + userText + " within 15 minutes. In the meantime, is there anything specific about your project you'd like us to know?";
        sendToWebhook({...capturedInfo, message: '', source: 'chatbot', timestamp: new Date().toISOString()});
      } else {
        // Normal chat flow
        if (lower.includes('price') || lower.includes('cost') || lower.includes('quote') || lower.includes('estimate')) {
          reply = "We offer free, no-obligation estimates! Andre will visit your property and give you an upfront quote. What's your name so we can get started?";
          step = 'ask_name';
        } else if (lower.includes('roof')) {
          reply = "We do roof installation, repairs, inspections, and full replacements. What type of roofing project do you have?";
        } else if (lower.includes('plumb')) {
          reply = "Our plumbers handle leaks, fixtures, drain clearing, and pipe work. Is this an emergency or scheduled repair?";
        } else if (lower.includes('electrical') || lower.includes('electric')) {
          reply = "We do outlets, panels, lighting, ceiling fans, and wiring. What's the electrical issue?";
        } else if (lower.includes('gutter')) {
          reply = "We clean, repair, and install seamless gutters with leaf guards. What's your gutter situation?";
        } else if (lower.includes('power wash') || lower.includes('pressure wash')) {
          reply = "We power wash decks, driveways, siding, and roofs. What surface needs cleaning?";
        } else if (lower.includes('deck') || lower.includes('siding')) {
          reply = "We build, repair, and refinish decks. We also install vinyl, wood, and fiber cement siding. What are you looking to do?";
        } else if (lower.includes('hour') || lower.includes('time') || lower.includes('open')) {
          reply = "We're open Monday–Friday 7AM–6PM and Saturday 8AM–4PM. Same-day service is often available!";
        } else if (lower.includes('area') || lower.includes('city') || lower.includes('serve')) {
          reply = "We serve Fredericksburg, Stafford, Woodbridge, King George, Caroline, and Culpeper. Which city are you in?";
        } else if (lower.includes('licensed') || lower.includes('insur')) {
          reply = "Yes! Dre Home Services is fully licensed and insured. We carry general liability and workers' comp for your protection.";
        } else if (lower.includes('andre')) {
          reply = "Andre is the owner and leads every project personally. 10+ years experience, 500+ happy homeowners.";
        } else if (lower.includes('call') || lower.includes('phone')) {
          reply = "You can call Andre directly at (804) 848-9575. Or leave your info and he'll call you back within 15 minutes!";
        } else if (lower.includes('help') || lower.includes('hi') || lower.includes('hello')) {
          reply = "Hi there! I can help with questions about roofing, plumbing, electrical, gutters, power washing, deck and siding. Or I can connect you with Andre for a free estimate. What do you need help with?";
        } else {
          reply = "I'm not sure about that, but Andre would know. Want me to connect you? Just tell me your name and what project you're working on, and he'll call you within 15 minutes. Or call (804) 848-9575 anytime.";
        }
      }

      setTimeout(() => addMessage(reply, true), 400);
    }

    function sendToWebhook(payload) {
      fetch(WEBHOOK_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'X-Nida-Secret': NIDA_SECRET },
        body: JSON.stringify(payload)
      }).catch(() => {});
    }

    function sendMessage() {
      const text = input.value.trim();
      if (!text) return;
      addMessage(text, false);
      input.value = '';
      botReply(text);
    }

    sendBtn.addEventListener('click', sendMessage);
    input.addEventListener('keypress', (e) => { if (e.key === 'Enter') sendMessage(); });
  })();

})();
