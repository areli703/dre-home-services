#!/usr/bin/env python3
"""Bulk generator for Dre Home Services support pages + city pages v2 (logo-matched, modal form, fixed hamburger)."""
import os

BASE = "/home/stephen/projects/dre-home-services"
COMPANY = "Dre Home Services LLC"
PHONE = "(804) 848-9575"
PHONE_RAW = "+18048489575"
EMAIL = "info@drehomeservicesllc.com"
DOMAIN = "https://areli703.github.io/dre-home-services"

cities = [
    ("fredericksburg", "Fredericksburg", "Spotsylvania County", "historic downtown and Civil War heritage", "colonial-era homes and modern subdivisions", "residential neighborhoods along the Rappahannock River"),
    ("king-george", "King George", "King George County", "peaceful rural communities near the Potomac", "single-family homes and waterfront properties", "Dahlgren and the Naval Surface Warfare Center area"),
    ("caroline", "Caroline", "Caroline County", "rolling countryside and farmland", "rural homes and acreage properties", "Bowling Green and Lake Caroline communities"),
    ("stafford", "Stafford", "Stafford County", "fast-growing suburbs with military roots", "new construction homes and established neighborhoods", "Aquia Harbour and Garrisonville communities"),
    ("culpeper", "Culpeper", "Culpeper County", "charming small-town atmosphere", "historic homes and countryside estates", "downtown Culpeper and the scenic Piedmont"),
    ("woodbridge", "Woodbridge", "Prince William County", "diverse neighborhoods near Occoquan", "townhouses, condos, and single-family homes", "Lake Ridge and Dale City communities"),
]

services_list = [
    ("roof-installation", "Roof Installation & Repairs", "roofing"),
    ("roof-inspection", "Roof Inspection", "inspection"),
    ("preventive-maintenance", "Preventive Maintenance", "maintenance"),
    ("waterproofing", "Waterproofing & Traffic Coating", "waterproofing"),
    ("gutter-cleaning", "Gutter Cleaning & Installation", "gutters"),
    ("powerwashing", "Power Washing", "powerwashing"),
    ("electrical", "Electrical", "electrical-plumbing"),
    ("plumbing", "Plumbing", "electrical-plumbing"),
    ("deck", "Deck & Siding", "deck-siding"),
]

def head(title, desc, canonical, depth=0):
    prefix = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}css/style.css">
</head>
<body>
<div class="sticky-cta"><div class="sticky-cta-inner"><a href="tel:{PHONE_RAW}" class="btn btn-dark">Call Now</a><button class="btn btn-primary" data-open-modal>Free Quote</button></div></div>
"""

def nav(prefix=""):
    logo_path = f"{prefix}images/logo.png"
    return f"""
<nav><div class="container nav-container"><a href="{prefix}index.html" class="nav-logo-link"><img src="{logo_path}" alt="Dre Home Services" class="nav-logo-img"></a><button class="mobile-menu-btn" aria-label="Toggle menu">&#9776;</button><ul class="nav-links"><li><a href="{prefix}services.html">Services</a></li><li><a href="{prefix}areas-we-serve.html">Areas We Serve</a></li><li><a href="{prefix}about.html">About</a></li><li><a href="{prefix}faq.html">FAQ</a></li><li><a href="{prefix}contact.html">Contact</a></li></ul><div class="nav-cta"><a href="tel:{PHONE_RAW}" class="phone-link">{PHONE}</a><button class="btn btn-primary" data-open-modal>Free Estimate</button></div></div><div class="mobile-nav"><ul><li><a href="{prefix}services.html">Services</a></li><li><a href="{prefix}areas-we-serve.html">Areas We Serve</a></li><li><a href="{prefix}about.html">About</a></li><li><a href="{prefix}faq.html">FAQ</a></li><li><a href="{prefix}contact.html">Contact</a></li><li><button class="btn btn-primary" data-open-modal style="width:100%;margin-top:16px;">Free Estimate</button></li></ul></div></nav>
"""

def modal_overlay(prefix=""):
    return f"""
<div class="modal-overlay" id="quote-modal">
  <div class="modal-content">
    <div class="modal-header">
      <div>
        <span class="section-label" style="margin-bottom:8px;">Get Started</span>
        <h2>Request a Free Estimate</h2>
      </div>
      <button class="modal-close" aria-label="Close">&times;</button>
    </div>
    <div class="modal-body">
      <form class="modal-form" id="quote-form">
        <div class="form-row">
          <div class="form-group"><label for="name">Full Name *</label><input type="text" id="name" name="name" required placeholder="John Smith"></div>
          <div class="form-group"><label for="phone">Phone Number *</label><input type="tel" id="phone" name="phone" required placeholder="(804) 555-1234"></div>
        </div>
        <div class="form-row">
          <div class="form-group"><label for="email">Email Address</label><input type="email" id="email" name="email" placeholder="john@email.com"></div>
          <div class="form-group"><label for="service">Service Needed *</label><select id="service" name="service" required><option value="">Select a service...</option><option value="roof-installation">Roof Installation</option><option value="roof-repair">Roof Repair</option><option value="roof-inspection">Roof Inspection</option><option value="preventive-maintenance">Preventive Maintenance</option><option value="waterproofing">Waterproofing / Coating</option><option value="gutter-cleaning">Gutter Cleaning</option><option value="gutter-installation">Gutter Installation</option><option value="powerwashing">Power Washing</option><option value="electrical">Electrical</option><option value="plumbing">Plumbing</option><option value="deck">Deck Construction / Repair</option><option value="siding">Siding</option><option value="other">Other / Multiple Services</option></select></div>
        </div>
        <div class="form-group"><label for="city">Your City *</label><select id="city" name="city" required><option value="">Select your city...</option><option value="Fredericksburg">Fredericksburg</option><option value="King George">King George</option><option value="Caroline">Caroline</option><option value="Stafford">Stafford</option><option value="Culpeper">Culpeper</option><option value="Woodbridge">Woodbridge</option><option value="Other">Other</option></select></div>
        <div class="form-group"><label for="message">Project Details</label><textarea id="message" name="message" placeholder="Tell us about your project, timeline, and any specific needs..."></textarea></div>
        <button type="submit" class="btn btn-primary btn-large">Get My Free Estimate</button>
        <p style="text-align:center;font-size:0.8rem;color:var(--text-muted);margin-top:16px;">Or call us directly at <a href="tel:{PHONE_RAW}">{PHONE}</a></p>
      </form>
      <div class="modal-success" id="modal-success">
        <div class="modal-success-icon">&#10003;</div>
        <h3 style="color:var(--brand-dark);margin-bottom:12px;">Quote Request Sent!</h3>
        <p style="color:var(--text-secondary);">Andre will call you within 24 hours.</p>
      </div>
    </div>
  </div>
</div>
"""

def cta_banner(prefix=""):
    return f"""
<section class="cta-banner"><div class="container reveal"><h2>Ready to Get Started?</h2><p>Call Dre Home Services today for a free, no-obligation estimate. We serve Fredericksburg, Stafford, Woodbridge, and all surrounding areas.</p><div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;"><button class="btn btn-primary btn-large" data-open-modal>Get Free Estimate</button><a href="tel:{PHONE_RAW}" class="btn btn-dark btn-large">Call {PHONE}</a></div></div></section>
"""

def footer(prefix=""):
    logo_path = f"{prefix}images/logo.png"
    return f"""
<footer><div class="container"><div class="footer-grid"><div><div class="footer-brand"><img src="{logo_path}" alt="Dre Home Services" class="footer-logo">Dre Home Services</div><p class="footer-desc">Professional roofing, plumbing, electrical, gutter, power washing, deck & siding services across Central Virginia. Free estimates. Licensed & insured.</p></div><div class="footer-col"><h4>Services</h4><ul><li><a href="{prefix}services.html#roofing">Roofing</a></li><li><a href="{prefix}services.html#inspection">Inspection</a></li><li><a href="{prefix}services.html#waterproofing">Waterproofing</a></li><li><a href="{prefix}services.html#gutters">Gutters</a></li><li><a href="{prefix}services.html#electrical-plumbing">Electrical & Plumbing</a></li></ul></div><div class="footer-col"><h4>Company</h4><ul><li><a href="{prefix}about.html">About</a></li><li><a href="{prefix}areas-we-serve.html">Areas</a></li><li><a href="{prefix}testimonials.html">Testimonials</a></li><li><a href="{prefix}faq.html">FAQ</a></li><li><a href="{prefix}contact.html">Contact</a></li></ul></div><div class="footer-col"><h4>Contact</h4><ul><li><a href="tel:{PHONE_RAW}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><button data-open-modal style="background:none;border:none;color:rgba(255,255,255,0.5);font-size:0.9rem;cursor:pointer;padding:0;">Free Estimate</button></li></ul></div></div><div class="footer-bottom"><span>&copy; 2026 Dre Home Services LLC</span><span><a href="{prefix}privacy.html" style="color:rgba(255,255,255,0.4);">Privacy</a> &middot; <a href="{prefix}terms.html" style="color:rgba(255,255,255,0.4);">Terms</a></span></div></div></footer>
<script src="{prefix}js/main.js"></script>
</body></html>
"""

def page_header(label, h1, p):
    return f"""
<header class="page-header"><div class="container reveal"><span class="section-label">{label}</span><h1>{h1}</h1><p>{p}</p></div></header>
"""

# --- City pages ---
def write_city_page(slug, city, county, d1, d2, d3):
    path = f"{BASE}/areas/{slug}.html"
    services_cards = ""
    for svc_slug, svc_name, svc_anchor in services_list:
        services_cards += f"""
<div class="service-card"><div class="service-icon">&#127968;</div><h3>{svc_name} in {city}</h3><p>Professional {svc_name.lower()} services for {city} homeowners and businesses. Free estimates, quality workmanship.</p><a href="../services.html#{svc_anchor}" class="service-link">Learn More &rarr;</a></div>
"""

    html = head(
        f"{COMPANY} | Home Services in {city}, {county} | Free Estimates",
        f"Professional home services in {city}, {county}. Roofing, plumbing, electrical, gutters, power washing, deck & siding. Free estimates. Call {PHONE}.",
        f"{DOMAIN}/areas/{slug}.html",
        depth=1
    ) + nav(prefix="../") + page_header(
        f"{city}, {county}",
        f"Home Services in {city}",
        f"Fast, professional home services serving {city} and surrounding {county} communities."
    ) + f"""
<section class="content-section"><div class="container">
<div class="reveal" style="display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center;">
  <div><span class="section-label">Local Service</span><h2 style="text-align:left;" class="section-title">Trusted Home Services in {city}</h2><p style="color:var(--text-secondary);line-height:1.7;margin-bottom:20px;">{COMPANY} proudly serves {city}, {d1}. We understand the unique needs of {d2} in this area and provide fast, reliable service with upfront pricing.</p><p style="color:var(--text-secondary);line-height:1.7;margin-bottom:20px;">Whether you are maintaining {d3} or tackling a major renovation, our local crew arrives on time, handles all the heavy lifting, and leaves your property in better shape than we found it. Every job is backed by our satisfaction guarantee.</p><div style="display:flex;gap:12px;margin-top:28px;flex-wrap:wrap;"><button class="btn btn-primary" data-open-modal>Get a Free Quote</button><a href="tel:{PHONE_RAW}" class="btn btn-dark">Call {PHONE}</a></div></div>
  <div class="service-card" style="padding:28px;"><h3 style="margin-bottom:16px;">Why {city} Chooses Us</h3><div style="display:flex;flex-direction:column;gap:14px;"><div style="display:flex;align-items:center;gap:10px;"><span style="color:var(--green-light);">&#10003;</span><span style="color:var(--text-secondary);font-size:0.9rem;">Same-day appointments available</span></div><div style="display:flex;align-items:center;gap:10px;"><span style="color:var(--green-light);">&#10003;</span><span style="color:var(--text-secondary);font-size:0.9rem;">Upfront, no-surprise pricing</span></div><div style="display:flex;align-items:center;gap:10px;"><span style="color:var(--green-light);">&#10003;</span><span style="color:var(--text-secondary);font-size:0.9rem;">Licensed & insured professionals</span></div><div style="display:flex;align-items:center;gap:10px;"><span style="color:var(--green-light);">&#10003;</span><span style="color:var(--text-secondary);font-size:0.9rem;">Free estimates on every project</span></div><div style="display:flex;align-items:center;gap:10px;"><span style="color:var(--green-light);">&#10003;</span><span style="color:var(--text-secondary);font-size:0.9rem;">Satisfaction guaranteed</span></div></div></div>
</div>
</div></section>

<section style="background:var(--bg-warm);"><div class="container">
<div class="section-header reveal"><span class="section-label">Services in {city}</span><h2 class="section-title">What We Do in {city}</h2></div>
<div class="services-grid reveal">
{services_cards}</div>
</div></section>

<section class="content-section"><div class="container">
<div class="section-header reveal"><span class="section-label">Nearby Areas</span><h2 class="section-title">We Also Serve Nearby {county} Communities</h2></div>
<div class="areas-grid reveal">
"""
    for other_slug, other_city, other_county, _, _, _ in cities:
        if other_slug != slug:
            html += f'<a href="{other_slug}.html" class="area-card"><h3>{other_city}</h3><p>{other_county}</p></a>\n'

    html += f"""
</div></div></section>

{cta_banner(prefix="../")}
{modal_overlay(prefix="../")}
{footer(prefix="../")}
"""
    with open(path, "w") as f:
        f.write(html)
    print(f"  areas/{slug}.html written")

# --- Support pages ---
def write_about():
    html = head(
        f"About Us | {COMPANY}",
        f"Meet Andre and the Dre Home Services team. Professional roofing, plumbing, electrical, and exterior services across Central Virginia since 2015.",
        f"{DOMAIN}/about.html"
    ) + nav() + page_header("Our Story", "About Dre Home Services", "A family-owned business built on quality workmanship, honest pricing, and treating every home like our own.") + f"""
<section class="content-section"><div class="container">
<div class="reveal" style="display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center;">
  <div><h2>Built on Trust, Backed by Skill</h2><p>Dre Home Services LLC was founded by Andre with a simple mission: provide reliable, high-quality home services that homeowners can trust. What started as a one-man roofing operation has grown into a full-service home improvement company serving Fredericksburg, Stafford, Woodbridge, and surrounding Central Virginia communities.</p><p>Every project — whether it's a minor plumbing fix or a full roof replacement — gets the same attention to detail. We show up on time, communicate clearly, and never leave a mess behind.</p><div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:32px;">
    <div class="service-card" style="text-align:center;padding:24px;"><div style="font-size:2rem;font-weight:800;color:var(--brand-orange);">10+</div><div style="font-size:0.9rem;color:var(--text-secondary);">Years Experience</div></div>
    <div class="service-card" style="text-align:center;padding:24px;"><div style="font-size:2rem;font-weight:800;color:var(--brand-orange);">500+</div><div style="font-size:0.9rem;color:var(--text-secondary);">Projects Completed</div></div>
    <div class="service-card" style="text-align:center;padding:24px;"><div style="font-size:2rem;font-weight:800;color:var(--brand-orange);">7</div><div style="font-size:0.9rem;color:var(--text-secondary);">Cities Served</div></div>
    <div class="service-card" style="text-align:center;padding:24px;"><div style="font-size:2rem;font-weight:800;color:var(--brand-orange);">100%</div><div style="font-size:0.9rem;color:var(--text-secondary);">Satisfaction Focused</div></div>
  </div></div>
  <div class="service-card" style="padding:40px;"><h3 style="margin-bottom:20px;">Our Core Values</h3><ul style="list-style:none;display:flex;flex-direction:column;gap:16px;color:var(--text-secondary);"><li><strong style="color:var(--brand-dark);">Honesty First</strong> — No upselling, no hidden fees. We quote what you need, not what pads our invoice.</li><li><strong style="color:var(--brand-dark);">Quality Craftsmanship</strong> — Every nail, pipe, and wire is installed to code and built to last.</li><li><strong style="color:var(--brand-dark);">Respect for Your Home</strong> — We treat your property like our own. Clean work sites, protective coverings, and thorough cleanup.</li><li><strong style="color:var(--brand-dark);">Reliable Communication</strong> — You'll always know when we're coming, what we're doing, and when we'll be done.</li></ul></div>
</div>
</div></section>
{cta_banner()}
{modal_overlay()}
{footer()}
"""
    with open(f"{BASE}/about.html", "w") as f:
        f.write(html)
    print("  about.html written")

def write_contact():
    html = head(
        f"Contact Us | {COMPANY}",
        f"Contact Dre Home Services LLC. Call {PHONE} or email {EMAIL}. Free estimates across Fredericksburg, Stafford, Woodbridge and surrounding areas.",
        f"{DOMAIN}/contact.html"
    ) + nav() + page_header("Get in Touch", "Contact Dre Home Services", "Have a question or ready to start your project? We're here to help.") + f"""
<section class="content-section"><div class="container">
<div class="reveal" style="display:grid;grid-template-columns:1fr 1fr;gap:48px;">
  <div><h2>Reach Out Anytime</h2><p>Whether you need an emergency repair, a routine inspection, or a major renovation quote, we're just a call or message away.</p>
  <div style="display:flex;flex-direction:column;gap:20px;margin-top:32px;">
    <div class="service-card"><div style="display:flex;align-items:center;gap:16px;"><div class="hero-card-icon">&#128222;</div><div><div style="font-weight:600;">Phone</div><a href="tel:{PHONE_RAW}">{PHONE}</a></div></div></div>
    <div class="service-card"><div style="display:flex;align-items:center;gap:16px;"><div class="hero-card-icon">&#9993;</div><div><div style="font-weight:600;">Email</div><a href="mailto:{EMAIL}">{EMAIL}</a></div></div></div>
    <div class="service-card"><div style="display:flex;align-items:center;gap:16px;"><div class="hero-card-icon">&#128205;</div><div><div style="font-weight:600;">Service Area</div><span style="color:var(--text-secondary);">Fredericksburg, King George, Caroline, Stafford, Culpeper, Woodbridge</span></div></div></div>
    <div class="service-card"><div style="display:flex;align-items:center;gap:16px;"><div class="hero-card-icon">&#128337;</div><div><div style="font-weight:600;">Hours</div><span style="color:var(--text-secondary);">Mon–Fri: 7AM–6PM | Sat: 8AM–4PM</span></div></div></div>
  </div></div>
  <div class="quote-form"><h3 style="margin-bottom:24px;color:var(--brand-dark);">Send a Message</h3>
  <form id="quote-form">
    <div class="form-group"><label for="name">Name</label><input type="text" id="name" name="name" required></div>
    <div class="form-row"><div class="form-group"><label for="email">Email</label><input type="email" id="email" name="email"></div><div class="form-group"><label for="phone">Phone</label><input type="tel" id="phone" name="phone" required></div></div>
    <div class="form-group"><label for="message">Message</label><textarea id="message" name="message" placeholder="How can we help you?"></textarea></div>
    <button type="submit" class="btn btn-primary btn-large form-submit">Send Message</button>
  </form></div>
</div>
</div></section>
{cta_banner()}
{modal_overlay()}
{footer()}
"""
    with open(f"{BASE}/contact.html", "w") as f:
        f.write(html)
    print("  contact.html written")

def write_faq():
    html = head(
        f"FAQ | {COMPANY}",
        f"Frequently asked questions about Dre Home Services. Pricing, scheduling, warranties, and more. Call {PHONE} for a free estimate.",
        f"{DOMAIN}/faq.html"
    ) + nav() + page_header("Common Questions", "Frequently Asked Questions", "Everything you need to know before starting your project.") + f"""
<section class="content-section"><div class="container" style="max-width:800px;">
<div class="reveal">
<div class="faq-item open"><div class="faq-question">Do you offer free estimates?<span class="faq-toggle">+</span></div><div class="faq-answer">Yes! Every project starts with a free, no-obligation estimate. Andre will visit your property, assess the work, and provide a detailed quote with no hidden fees or pressure.</div></div>
<div class="faq-item"><div class="faq-question">Are you licensed and insured?<span class="faq-toggle">+</span></div><div class="faq-answer">Absolutely. Dre Home Services LLC is fully licensed and insured for all the services we provide. We carry general liability insurance and workers' compensation coverage for your protection and ours.</div></div>
<div class="faq-item"><div class="faq-question">What areas do you serve?<span class="faq-toggle">+</span></div><div class="faq-answer">We serve Fredericksburg, King George, Caroline, Stafford, Culpeper, Woodbridge, and surrounding communities in Central Virginia. If you're unsure whether we cover your area, just give us a call.</div></div>
<div class="faq-item"><div class="faq-question">How quickly can you start my project?<span class="faq-toggle">+</span></div><div class="faq-answer">For most repairs and smaller jobs, we can schedule within 1–3 business days. Larger projects like full roof replacements may require 1–2 weeks for material ordering. Emergency repairs are prioritized.</div></div>
<div class="faq-item"><div class="faq-question">Do you warranty your work?<span class="faq-toggle">+</span></div><div class="faq-answer">Yes. We stand behind our craftsmanship with workmanship warranties on all installations and repairs. Material warranties vary by manufacturer and are passed directly to you. We'll explain all warranty details before starting any work.</div></div>
<div class="faq-item"><div class="faq-question">Can I get a roof inspection for insurance purposes?<span class="faq-toggle">+</span></div><div class="faq-answer">Yes. Our roof inspections include photo documentation, detailed condition reports, and damage assessments that meet insurance company requirements. We can also meet with your adjuster if needed.</div></div>
<div class="faq-item"><div class="faq-question">What payment options do you accept?<span class="faq-toggle">+</span></div><div class="faq-answer">We accept cash, checks, and all major credit cards. For larger projects, we offer flexible payment schedules — typically a deposit to secure materials, with the balance due upon completion.</div></div>
<div class="faq-item"><div class="faq-question">Do you clean up after the job?<span class="faq-toggle">+</span></div><div class="faq-answer">Always. We use protective coverings, magnetic nail sweepers, and thorough cleanup protocols. Your property will be left in the same condition — or better — than when we arrived.</div></div>
</div>
</div></section>
{cta_banner()}
{modal_overlay()}
{footer()}
"""
    with open(f"{BASE}/faq.html", "w") as f:
        f.write(html)
    print("  faq.html written")

def write_testimonials():
    html = head(
        f"Testimonials | {COMPANY}",
        f"Read reviews from Dre Home Services customers across Fredericksburg, Stafford, Woodbridge and beyond. 5-star service, guaranteed satisfaction.",
        f"{DOMAIN}/testimonials.html"
    ) + nav() + page_header("Customer Reviews", "What Our Customers Say", "Real reviews from real homeowners across Central Virginia.") + f"""
<section class="testimonials" style="padding-top:60px;"><div class="container">
<div class="reviews-grid reveal">
  <div class="review-card"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p class="review-text">"Andre and his crew replaced our entire roof in two days. Cleaned up everything, and the price was fair. Highly recommend Dre Home Services!"</p><div class="review-author">Marcus T.</div><div class="review-location">Fredericksburg, VA</div></div>
  <div class="review-card"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p class="review-text">"Fixed a leak in our bathroom plumbing same day I called. Professional, courteous, and didn't try to upsell me on things I didn't need."</p><div class="review-author">Jennifer L.</div><div class="review-location">Stafford, VA</div></div>
  <div class="review-card"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p class="review-text">"Had our gutters cleaned and new downspouts installed. Great work, fair price, and they showed up exactly when they said they would."</p><div class="review-author">Robert K.</div><div class="review-location">Woodbridge, VA</div></div>
  <div class="review-card"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p class="review-text">"The power washing made our deck look brand new. They were careful with the wood and even pointed out a loose board they fixed while they were here."</p><div class="review-author">Angela M.</div><div class="review-location">King George, VA</div></div>
  <div class="review-card"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p class="review-text">"Andre inspected our roof before we sold our house. His report was thorough and helped us negotiate confidently with the buyer."</p><div class="review-author">David P.</div><div class="review-location">Culpeper, VA</div></div>
  <div class="review-card"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p class="review-text">"Had them do electrical work in our kitchen and a small plumbing repair. Both done same day, up to code, and at a fair price. Will definitely call again."</p><div class="review-author">Lisa R.</div><div class="review-location">Caroline, VA</div></div>
</div>
</div></section>
{cta_banner()}
{modal_overlay()}
{footer()}
"""
    with open(f"{BASE}/testimonials.html", "w") as f:
        f.write(html)
    print("  testimonials.html written")

def write_areas_we_serve():
    html = head(
        f"Areas We Serve | {COMPANY}",
        f"Dre Home Services serves Fredericksburg, King George, Caroline, Stafford, Culpeper, Woodbridge and surrounding areas. Free estimates. Call {PHONE}.",
        f"{DOMAIN}/areas-we-serve.html"
    ) + nav() + page_header("Service Area", "Areas We Serve", "Proudly providing professional home services across Central Virginia.") + f"""
<section class="content-section"><div class="container">
<div class="reveal" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;">
  <a href="areas/fredericksburg.html" class="area-card" style="text-align:left;padding:32px;"><h3>Fredericksburg</h3><p style="margin:0 0 12px;">Spotsylvania County</p><p style="font-size:0.85rem;">Historic downtown, modern subdivisions, and neighborhoods along the Rappahannock River.</p></a>
  <a href="areas/king-george.html" class="area-card" style="text-align:left;padding:32px;"><h3>King George</h3><p style="margin:0 0 12px;">King George County</p><p style="font-size:0.85rem;">Rural communities, waterfront properties, and the Dahlgren area.</p></a>
  <a href="areas/caroline.html" class="area-card" style="text-align:left;padding:32px;"><h3>Caroline</h3><p style="margin:0 0 12px;">Caroline County</p><p style="font-size:0.85rem;">Rolling countryside, farmland, and the Bowling Green community.</p></a>
  <a href="areas/stafford.html" class="area-card" style="text-align:left;padding:32px;"><h3>Stafford</h3><p style="margin:0 0 12px;">Stafford County</p><p style="font-size:0.85rem;">Fast-growing suburbs, military families, and new construction.</p></a>
  <a href="areas/culpeper.html" class="area-card" style="text-align:left;padding:32px;"><h3>Culpeper</h3><p style="margin:0 0 12px;">Culpeper County</p><p style="font-size:0.85rem;">Historic small-town charm, countryside estates, and scenic Piedmont.</p></a>
  <a href="areas/woodbridge.html" class="area-card" style="text-align:left;padding:32px;"><h3>Woodbridge</h3><p style="margin:0 0 12px;">Prince William County</p><p style="font-size:0.85rem;">Diverse neighborhoods near Occoquan, Lake Ridge, and Dale City.</p></a>
</div>
<div class="reveal" style="text-align:center;margin-top:48px;">
  <p style="font-size:1.1rem;max-width:600px;margin:0 auto 24px;">Don't see your city? We often travel beyond these areas for larger projects. Give us a call and we'll let you know if we can help.</p>
  <a href="tel:{PHONE_RAW}" class="btn btn-primary btn-large">Call {PHONE}</a>
</div>
</div></section>
{cta_banner()}
{modal_overlay()}
{footer()}
"""
    with open(f"{BASE}/areas-we-serve.html", "w") as f:
        f.write(html)
    print("  areas-we-serve.html written")

def write_quote():
    # quote.html now just opens the modal on load and shows a brief page
    html = head(
        f"Free Estimate | {COMPANY}",
        f"Request a free estimate from Dre Home Services. Roofing, plumbing, electrical, gutters, power washing, deck & siding. Call {PHONE}.",
        f"{DOMAIN}/quote.html"
    ) + nav() + f"""
<header class="page-header"><div class="container reveal"><span class="section-label">Get Started</span><h1>Request a Free Estimate</h1><p>Tell us about your project and we'll get back to you within 24 hours.</p></div></header>
<section class="content-section"><div class="container text-center reveal" style="max-width:600px;">
  <p style="font-size:1.1rem;margin-bottom:32px;">Click the button below to open our quick estimate form. It only takes 60 seconds.</p>
  <button class="btn btn-primary btn-large" data-open-modal style="margin-bottom:16px;">Open Quote Form</button>
  <p style="color:var(--text-muted);font-size:0.9rem;">Or call us directly at <a href="tel:{PHONE_RAW}">{PHONE}</a></p>
</div></section>
{cta_banner()}
{modal_overlay()}
{footer()}
"""
    with open(f"{BASE}/quote.html", "w") as f:
        f.write(html)
    print("  quote.html written")

def write_privacy():
    html = head(
        f"Privacy Policy | {COMPANY}",
        f"Privacy Policy for Dre Home Services LLC. How we collect, use, and protect your personal information.",
        f"{DOMAIN}/privacy.html"
    ) + nav() + page_header("Legal", "Privacy Policy", "Your privacy matters to us. Here's how we handle your information.") + f"""
<section class="content-section"><div class="container" style="max-width:800px;">
<div class="reveal">
<p style="margin-bottom:24px;"><strong>Last updated:</strong> June 1, 2026</p>
<h3>1. Information We Collect</h3><p>We collect information you provide through our quote form, including your name, phone number, email address, city, service requested, and project details. We may also collect information about how you interact with our website.</p>
<h3>2. How We Use Your Information</h3><p>We use your information to respond to quote requests, schedule appointments, communicate about your project, and improve our services. We do not sell or rent your personal information to third parties.</p>
<h3>3. Information Sharing</h3><p>We may share your information with trusted service providers who assist us in operating our website or servicing you (e.g., CRM systems). All providers are bound by confidentiality agreements.</p>
<h3>4. Data Security</h3><p>We implement reasonable security measures to protect your personal information. However, no method of transmission over the internet is 100% secure.</p>
<h3>5. Your Choices</h3><p>You may contact us at any time to update, correct, or delete your personal information. Email {EMAIL} or call {PHONE}.</p>
<h3>6. Cookies</h3><p>We may use cookies to enhance your browsing experience. You can set your browser to refuse cookies.</p>
<h3>7. Contact Us</h3><p>If you have questions about this privacy policy, contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> or <a href="tel:{PHONE_RAW}">{PHONE}</a>.</p>
</div>
</div></section>
{modal_overlay()}
{footer()}
"""
    with open(f"{BASE}/privacy.html", "w") as f:
        f.write(html)
    print("  privacy.html written")

def write_terms():
    html = head(
        f"Terms of Service | {COMPANY}",
        f"Terms of Service for Dre Home Services LLC. Using our website and services.",
        f"{DOMAIN}/terms.html"
    ) + nav() + page_header("Legal", "Terms of Service", "By using our website and services, you agree to these terms.") + f"""
<section class="content-section"><div class="container" style="max-width:800px;">
<div class="reveal">
<p style="margin-bottom:24px;"><strong>Last updated:</strong> June 1, 2026</p>
<h3>1. Acceptance of Terms</h3><p>By accessing or using our website, you agree to be bound by these Terms of Service. If you do not agree, please do not use our website.</p>
<h3>2. Services</h3><p>Dre Home Services LLC provides roofing, plumbing, electrical, gutter, power washing, deck, and siding services. All work is subject to a written estimate and contract.</p>
<h3>3. Quotes and Estimates</h3><p>Online quote requests are for estimation purposes only. Final pricing is provided after an on-site inspection. Estimates are valid for 30 days unless otherwise stated.</p>
<h3>4. Payment Terms</h3><p>Payment terms are specified in your service contract. Typically, a deposit is required for material ordering, with the balance due upon project completion.</p>
<h3>5. Warranties</h3><p>Workmanship warranties are provided as specified in your contract. Material warranties are provided by the manufacturer and passed through to you.</p>
<h3>6. Limitation of Liability</h3><p>Our liability is limited to the amount paid for the specific service in question. We are not liable for indirect, incidental, or consequential damages.</p>
<h3>7. Changes to Terms</h3><p>We may update these terms at any time. Continued use of the website constitutes acceptance of revised terms.</p>
<h3>8. Contact</h3><p>Questions about these terms? Contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> or <a href="tel:{PHONE_RAW}">{PHONE}</a>.</p>
</div>
</div></section>
{modal_overlay()}
{footer()}
"""
    with open(f"{BASE}/terms.html", "w") as f:
        f.write(html)
    print("  terms.html written")

def write_sitemap():
    pages = [
        ("", "Homepage"),
        ("services.html", "Services"),
        ("about.html", "About Us"),
        ("areas-we-serve.html", "Areas We Serve"),
        ("testimonials.html", "Testimonials"),
        ("faq.html", "FAQ"),
        ("contact.html", "Contact"),
        ("quote.html", "Free Estimate"),
        ("privacy.html", "Privacy Policy"),
        ("terms.html", "Terms of Service"),
    ]
    for slug, city, county, _, _, _ in cities:
        pages.append((f"areas/{slug}.html", f"{city} — {county}"))

    links = "\n".join([f'<li style="margin-bottom:8px;"><a href="{url}">{title}</a></li>' for url, title in pages])
    html = head(
        f"Sitemap | {COMPANY}",
        f"Complete sitemap for Dre Home Services LLC. All pages and services.",
        f"{DOMAIN}/sitemap.html"
    ) + nav() + page_header("Navigation", "Sitemap", "All pages on the Dre Home Services website.") + f"""
<section class="content-section"><div class="container" style="max-width:800px;">
<div class="reveal">
<ul style="list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:8px;">
{links}
</ul>
</div>
</div></section>
{modal_overlay()}
{footer()}
"""
    with open(f"{BASE}/sitemap.html", "w") as f:
        f.write(html)
    print("  sitemap.html written")

def write_xml_sitemap():
    pages = [
        ("", "1.0"),
        ("services.html", "0.9"),
        ("about.html", "0.8"),
        ("areas-we-serve.html", "0.8"),
        ("quote.html", "0.9"),
        ("testimonials.html", "0.7"),
        ("faq.html", "0.7"),
        ("contact.html", "0.7"),
        ("privacy.html", "0.3"),
        ("terms.html", "0.3"),
        ("sitemap.html", "0.3"),
    ]
    for slug, city, county, _, _, _ in cities:
        pages.append((f"areas/{slug}.html", "0.8"))

    urls = "\n".join([f"  <url><loc>{DOMAIN}/{url}</loc><lastmod>2026-06-01</lastmod><changefreq>weekly</changefreq><priority>{priority}</priority></url>" for url, priority in pages])

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>"""
    with open(f"{BASE}/sitemap.xml", "w") as f:
        f.write(xml)
    print("  sitemap.xml written")

def write_robots():
    txt = f"""User-agent: *
Allow: /
Sitemap: {DOMAIN}/sitemap.xml"""
    with open(f"{BASE}/robots.txt", "w") as f:
        f.write(txt)
    print("  robots.txt written")

# --- Run everything ---
if __name__ == "__main__":
    os.makedirs(f"{BASE}/areas", exist_ok=True)

    for slug, city, county, d1, d2, d3 in cities:
        write_city_page(slug, city, county, d1, d2, d3)

    write_about()
    write_contact()
    write_faq()
    write_testimonials()
    write_areas_we_serve()
    write_quote()
    write_privacy()
    write_terms()
    write_sitemap()
    write_xml_sitemap()
    write_robots()

    print(f"\nDone. {len(cities)} city pages + 10 support pages generated.")
    print(f"Total pages: {len(cities) + 10}")
