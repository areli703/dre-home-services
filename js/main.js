/* Dre Home Services — Main JS */

// Enable JS-only scroll reveals
document.body.classList.add('js-on');

// ---- Scroll Reveal with IntersectionObserver ----
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// ---- Mobile Nav ----
const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
const mobileNav = document.querySelector('.mobile-nav');
if (mobileMenuBtn && mobileNav) {
  mobileMenuBtn.addEventListener('click', () => {
    mobileNav.classList.toggle('open');
  });
  mobileNav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => mobileNav.classList.remove('open'));
  });
}

// ---- FAQ Accordion ----
document.querySelectorAll('.faq-question').forEach(q => {
  q.addEventListener('click', () => {
    const item = q.parentElement;
    const wasOpen = item.classList.contains('open');
    // Close all
    document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
    // Open clicked if it wasn't open
    if (!wasOpen) item.classList.add('open');
  });
});

// ---- Quote Form: POST to Nida Webhook ----
const quoteForm = document.getElementById('quote-form');
if (quoteForm) {
  quoteForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const submitBtn = quoteForm.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Sending...';
    submitBtn.disabled = true;

    const formData = new FormData(quoteForm);
    const payload = {
      name: formData.get('name'),
      phone: formData.get('phone'),
      email: formData.get('email'),
      service: formData.get('service'),
      city: formData.get('city'),
      message: formData.get('message'),
      source: window.location.href,
      submitted_at: new Date().toISOString()
    };

    // TODO: Replace with actual Nida webhook URL once workspace is ready
    const WEBHOOK_URL = 'https://YOUR_NIDA_WEBHOOK_URL_HERE';

    try {
      // For now, show success message (webhook will be wired up later)
      console.log('Form payload:', payload);

      /*
      const res = await fetch(WEBHOOK_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      if (!res.ok) throw new Error('Webhook failed');
      */

      quoteForm.innerHTML = `
        <div style="text-align:center;padding:40px 0;">
          <div style="font-size:3rem;margin-bottom:16px;">&#9989;</div>
          <h3 style="color:var(--brand-navy);margin-bottom:12px;">Quote Request Sent!</h3>
          <p style="color:var(--text-secondary);">Andre will call you within 24 hours at ${payload.phone}.</p>
        </div>
      `;
    } catch (err) {
      submitBtn.textContent = originalText;
      submitBtn.disabled = false;
      alert('Something went wrong. Please call (804) 848-9575 directly.');
    }
  });
}

// ---- Smooth scroll for anchor links ----
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// ---- Phone link analytics placeholder ----
document.querySelectorAll('a[href^="tel:"]').forEach(link => {
  link.addEventListener('click', () => {
    // Could send event to analytics here
    console.log('Phone call initiated:', link.href);
  });
});
