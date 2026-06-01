/* Dre Home Services LLC — Main JS v2 */

// ---- Enable JS-only scroll reveals ----
document.body.classList.add('js-on');

// ---- Scroll Reveal ----
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// ---- Mobile Nav (Hamburger) ----
const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
const mobileNav = document.querySelector('.mobile-nav');

function toggleMobileMenu() {
  if (!mobileNav) return;
  const isOpen = mobileNav.classList.contains('open');
  if (isOpen) {
    mobileNav.classList.remove('open');
    document.body.style.overflow = '';
  } else {
    mobileNav.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
}

if (mobileMenuBtn && mobileNav) {
  mobileMenuBtn.addEventListener('click', (e) => {
    e.preventDefault();
    e.stopPropagation();
    toggleMobileMenu();
  });

  // Close when clicking a link
  mobileNav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      mobileNav.classList.remove('open');
      document.body.style.overflow = '';
    });
  });

  // Close when clicking outside
  document.addEventListener('click', (e) => {
    if (mobileNav.classList.contains('open') &&
        !mobileNav.contains(e.target) &&
        !mobileMenuBtn.contains(e.target)) {
      mobileNav.classList.remove('open');
      document.body.style.overflow = '';
    }
  });
}

// ---- FAQ Accordion ----
document.querySelectorAll('.faq-question').forEach(q => {
  q.addEventListener('click', () => {
    const item = q.parentElement;
    const wasOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
    if (!wasOpen) item.classList.add('open');
  });
});

// ---- Modal / Overlay Form ----
const modalOverlay = document.getElementById('quote-modal');
const modalCloseBtns = document.querySelectorAll('.modal-close, .modal-overlay');
const quoteForm = document.getElementById('quote-form');
const modalSuccess = document.getElementById('modal-success');

function openModal() {
  if (!modalOverlay) return;
  modalOverlay.classList.add('active');
  document.body.style.overflow = 'hidden';
  // Reset form state
  if (quoteForm) quoteForm.style.display = 'block';
  if (modalSuccess) modalSuccess.classList.remove('active');
}

function closeModal() {
  if (!modalOverlay) return;
  modalOverlay.classList.remove('active');
  document.body.style.overflow = '';
}

// Open modal from any trigger button
document.querySelectorAll('[data-open-modal]').forEach(btn => {
  btn.addEventListener('click', (e) => {
    e.preventDefault();
    openModal();
  });
});

// Close from X button or overlay click
if (modalOverlay) {
  modalOverlay.addEventListener('click', (e) => {
    if (e.target === modalOverlay || e.target.closest('.modal-close')) {
      closeModal();
    }
  });
}

// Close on Escape key
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && modalOverlay && modalOverlay.classList.contains('active')) {
    closeModal();
  }
});

// ---- Form Submit → Nida Webhook ----
if (quoteForm) {
  quoteForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const submitBtn = quoteForm.querySelector('button[type="submit"]');
    const originalText = submitBtn ? submitBtn.textContent : 'Submit';
    if (submitBtn) {
      submitBtn.textContent = 'Sending...';
      submitBtn.disabled = true;
    }

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

    // TODO: Replace with actual Nida webhook URL
    const WEBHOOK_URL = 'https://YOUR_NIDA_WEBHOOK_URL_HERE';

    try {
      console.log('Form payload:', payload);

      /*
      const res = await fetch(WEBHOOK_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      if (!res.ok) throw new Error('Webhook failed');
      */

      // Show success state in modal
      quoteForm.style.display = 'none';
      if (modalSuccess) modalSuccess.classList.add('active');

      // Auto-close after 4 seconds
      setTimeout(() => {
        closeModal();
      }, 4000);

    } catch (err) {
      if (submitBtn) {
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
      }
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

// ---- Phone link tracking placeholder ----
document.querySelectorAll('a[href^="tel:"]').forEach(link => {
  link.addEventListener('click', () => {
    console.log('Phone call initiated:', link.href);
  });
});
