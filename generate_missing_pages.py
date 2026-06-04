#!/usr/bin/env python3
"""Generate missing service pages and city+service combo pages for Dre Home Services."""
import os, json

BASE = "/home/stephen/dre-home-services-fix"
COMPANY = "Dre Home Services LLC"
PHONE = "(804) 848-9575"
PHONE_RAW = "+180****9575"
EMAIL = "info@drehomeservicesllc.com"
DOMAIN = "https://www.drehomeservicesllc.com"

cities = [
    ("fredericksburg", "Fredericksburg", "Spotsylvania County", "historic downtown and Civil War heritage", "colonial-era homes and modern subdivisions", "residential neighborhoods along the Rappahannock River", "Virginia's most historic city, with a mix of 18th-century landmarks and booming new developments"),
    ("king-george", "King George", "King George County", "peaceful rural communities near the Potomac", "single-family homes and waterfront properties", "Dahlgren and the Naval Surface Warfare Center area", "a serene riverside community with spacious lots and strong military family presence"),
    ("caroline", "Caroline", "Caroline County", "rolling countryside and farmland", "rural homes and acreage properties", "Bowling Green and Lake Caroline communities", "Virginia's quiet countryside, perfect for homesteaders and those seeking open space"),
    ("stafford", "Stafford", "Stafford County", "fast-growing suburbs with military roots", "new construction homes and established neighborhoods", "Aquia Harbour and Garrisonville communities", "one of Virginia's fastest-growing counties, with top schools and commuter-friendly access to DC"),
    ("culpeper", "Culpeper", "Culpeper County", "charming small-town atmosphere", "historic homes and countryside estates", "downtown Culpeper and the scenic Piedmont", "a picturesque small town with award-winning Main Street and thriving local businesses"),
    ("woodbridge", "Woodbridge", "Prince William County", "diverse neighborhoods near Occoquan", "townhouses, condos, and single-family homes", "Lake Ridge and Dale City communities", "a vibrant suburb with shopping, dining, and easy access to both DC and Richmond"),
]

services = [
    {
        "slug": "roof-installation",
        "name": "Roof Installation & Repairs",
        "short": "Roofing",
        "headline": "Expert Roof Installation & Repair Services",
        "description": "Complete roofing solutions including asphalt shingle, metal, and flat roof installation. Leak detection, storm damage restoration, flashing repairs, and emergency tarping. All work backed by workmanship warranties.",
        "features": ["Asphalt shingle, metal & flat roof installation", "Leak detection & emergency repair", "Storm damage & hail restoration", "Flashing, vent & chimney repairs", "Insurance claim documentation"],
        "keywords": "roof installation, roof repair, shingle replacement, metal roofing, flat roof, leak repair, storm damage, emergency roofing, Fredericksburg roofer, Stafford roofing contractor",
        "schema_cat": "RoofingContractor",
    },
    {
        "slug": "roof-inspection",
        "name": "Roof Inspection",
        "short": "Inspection",
        "headline": "Professional Roof Inspections You Can Trust",
        "description": "Thorough roof inspections for home buyers, sellers, and insurance claims. Photo documentation, detailed condition reports, and damage assessments that meet insurance requirements.",
        "features": ["Pre-purchase buyer inspections", "Pre-sale seller inspections", "Insurance claim documentation", "Annual condition assessments", "Hail & storm damage evaluation"],
        "keywords": "roof inspection, home buyer roof inspection, insurance roof inspection, roof condition report, pre-sale inspection, hail damage assessment, roof certification",
        "schema_cat": "HomeInspector",
    },
    {
        "slug": "preventive-maintenance",
        "name": "Preventive Maintenance",
        "short": "Maintenance",
        "headline": "Keep Your Home in Peak Condition Year-Round",
        "description": "Scheduled maintenance plans to catch small problems before they become expensive emergencies. Seasonal checks, gutter clearing, sealant inspection, and minor repairs.",
        "features": ["Seasonal roof checks & cleaning", "Gutter clearing & downspout flushing", "Caulking & sealant inspection", "Minor repairs & shingle replacement", "Moss & algae treatment"],
        "keywords": "home maintenance, roof maintenance plan, seasonal home check, gutter maintenance, preventive home care, property maintenance services",
        "schema_cat": "HomeAndConstructionBusiness",
    },
    {
        "slug": "waterproofing",
        "name": "Waterproofing & Traffic Coating",
        "short": "Waterproofing",
        "headline": "Advanced Waterproofing & Protective Coatings",
        "description": "Protect your property from water damage with professional waterproofing and traffic coating services. Basement sealing, flat roof membranes, deck coatings, and crack injection.",
        "features": ["Basement & foundation sealing", "Flat roof membrane systems", "Traffic-bearing deck coatings", "Balcony & terrace waterproofing", "Crack injection & repair"],
        "keywords": "waterproofing, basement waterproofing, foundation sealing, deck coating, flat roof membrane, traffic coating, crack injection, moisture barrier",
        "schema_cat": "HomeAndConstructionBusiness",
    },
    {
        "slug": "gutter-cleaning",
        "name": "Gutter Cleaning & Installation",
        "short": "Gutters",
        "headline": "Gutter Cleaning, Repair & Seamless Installation",
        "description": "Prevent water damage with professional gutter services. Cleaning, repair, seamless installation, downspout redirecting, and leaf guard systems to protect your foundation.",
        "features": ["Gutter cleaning & debris removal", "Seamless gutter installation", "Downspout repair & redirecting", "Gutter guard / leaf protection", "Gutter realignment & sealing"],
        "keywords": "gutter cleaning, gutter installation, seamless gutters, gutter repair, downspout installation, gutter guards, leaf protection, gutter maintenance",
        "schema_cat": "HomeAndConstructionBusiness",
    },
    {
        "slug": "powerwashing",
        "name": "Power Washing",
        "short": "Power Washing",
        "headline": "Restore Your Home's Curb Appeal",
        "description": "Professional power washing for houses, decks, driveways, roofs, and fences. Safe pressure techniques and eco-friendly cleaning agents for every surface type.",
        "features": ["House & siding washing", "Deck & patio restoration", "Driveway & walkway cleaning", "Roof moss & algae removal", "Fence & outdoor structure cleaning"],
        "keywords": "power washing, pressure washing, house washing, deck cleaning, driveway cleaning, roof cleaning, siding wash, fence cleaning, exterior cleaning",
        "schema_cat": "HomeAndConstructionBusiness",
    },
    {
        "slug": "electrical",
        "name": "Electrical Services",
        "short": "Electrical",
        "headline": "Licensed Electrical Services for Your Home",
        "description": "Safe, code-compliant electrical work from outlet installs to panel upgrades. All work performed by qualified professionals with proper permits when required.",
        "features": ["Outlet & switch installation/repair", "Ceiling fan & light fixture installs", "Panel upgrades & circuit work", "Wiring for renovations & additions", "Emergency electrical repairs"],
        "keywords": "electrician, electrical contractor, panel upgrade, outlet installation, ceiling fan install, wiring, electrical repair, licensed electrician, home electrical",
        "schema_cat": "Electrician",
    },
    {
        "slug": "plumbing",
        "name": "Plumbing Services",
        "short": "Plumbing",
        "headline": "Reliable Plumbing Repairs & Installations",
        "description": "From leaky faucets to full pipe replacements. Fast, reliable plumbing services with upfront pricing. Emergency repairs available.",
        "features": ["Leak detection & pipe repair", "Faucet, toilet & fixture installs", "Drain clearing & maintenance", "Water heater repair & replacement", "Emergency plumbing repairs"],
        "keywords": "plumber, plumbing repair, leak detection, drain clearing, toilet install, faucet repair, water heater, emergency plumber, pipe repair",
        "schema_cat": "Plumber",
    },
    {
        "slug": "deck",
        "name": "Deck & Siding",
        "short": "Deck & Siding",
        "headline": "Custom Decks & Quality Siding Installation",
        "description": "Build or restore your outdoor space. Custom deck design and construction, plus vinyl, wood, and fiber cement siding installation and repair.",
        "features": ["Custom deck design & construction", "Deck repair & board replacement", "Deck staining & sealing", "Vinyl siding installation & repair", "Fiber cement & wood siding"],
        "keywords": "deck builder, deck construction, deck repair, siding installation, vinyl siding, fiber cement siding, deck staining, wood deck, custom deck",
        "schema_cat": "HomeAndConstructionBusiness",
    },
]

def head(title, desc, canonical, depth=0, keywords="", og_title="", og_desc=""):
    prefix = "../" * depth
    if not og_title:
        og_title = title
    if not og_desc:
        og_desc = desc
    kw = f'<meta name="keywords" content="{keywords}">\n' if keywords else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
{kw}<meta name="author" content="{COMPANY}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<meta name="geo.region" content="US-VA">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/png" href="{prefix}images/favicon.png">
<link rel="apple-touch-icon" href="{prefix}images/favicon.png">
<meta name="theme-color" content="#D06000">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{COMPANY}">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMAIN}/images/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{og_desc}">
<meta name="twitter:image" content="{DOMAIN}/images/og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800;0,9..40,900;1,9..40,300;1,9..40,400&family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}css/style.css">
</head>
<body>
<div class="sticky-cta"><div class="sticky-cta-inner"><a href="tel:{PHONE_RAW}" class="btn btn-dark">Call Now</a><button class="btn btn-primary" data-open-modal>Free Quote</button></div></div>
"""

def nav(prefix=""):
    return f"""
<nav><div class="container nav-container"><a href="{prefix}" class="nav-logo-link"><img src="{prefix}images/logo.png" alt="Dre Home Services" class="nav-logo-img"></a><button class="mobile-menu-btn" aria-label="Toggle menu">&#9776;</button><ul class="nav-links"><li><a href="{prefix}services">Services</a></li><li><a href="{prefix}areas-we-serve">Areas We Serve</a></li><li><a href="{prefix}about">About</a></li><li><a href="{prefix}faq">FAQ</a></li><li><a href="{prefix}blog/index">Blog</a></li><li><a href="{prefix}contact">Contact</a></li></ul><div class="nav-cta"><a href="tel:{PHONE_RAW}" class="phone-link">{PHONE}</a><button class="btn btn-primary" data-open-modal>Free Estimate</button></div></div><div class="mobile-nav"><ul><li><a href="{prefix}services">Services</a></li><li><a href="{prefix}areas-we-serve">Areas We Serve</a></li><li><a href="{prefix}about">About</a></li><li><a href="{prefix}faq">FAQ</a></li><li><a href="{prefix}blog/index">Blog</a></li><li><a href="{prefix}contact">Contact</a></li><li><button class="btn btn-primary" data-open-modal style="width:100%;margin-top:16px;">Free Estimate</button></li></ul></div></nav>
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
        <button type="submit" class="btn btn-primary btn-large btn-glow">Get My Free Estimate</button>
        <p style="text-align:center;font-size:0.85rem;color:var(--text-muted);margin-top:16px;">Or call us directly at <a href="tel:{PHONE_RAW}">{PHONE}</a></p>
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
<section class="cta-banner"><div class="container"><h2 class="sr">Ready to Get Started?</h2><p class="sr sr-delay-1">Call Dre Home Services today for a free, no-obligation estimate. We serve Fredericksburg, Stafford, Woodbridge, and all surrounding areas.</p><div class="sr sr-delay-2" style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;"><button class="btn btn-primary btn-large btn-glow" data-open-modal>Get Free Estimate</button><a href="tel:{PHONE_RAW}" class="btn btn-outline btn-large">Call {PHONE}</a></div></div></section>
"""

def footer(prefix=""):
    return f"""
<footer><div class="container"><div class="footer-grid"><div><div class="footer-brand"><img src="{prefix}images/logo.png" alt="Dre Home Services" class="footer-logo">Dre Home Services</div><p class="footer-desc">Professional roofing, plumbing, electrical, gutter, power washing, deck & siding services across Central Virginia. Free estimates. Licensed & insured.</p></div><div class="footer-col"><h4>Services</h4><ul><li><a href="{prefix}services">Roofing</a></li><li><a href="{prefix}services">Inspection</a></li><li><a href="{prefix}services">Waterproofing</a></li><li><a href="{prefix}services">Gutters</a></li><li><a href="{prefix}services">Electrical & Plumbing</a></li></ul></div><div class="footer-col"><h4>Company</h4><ul><li><a href="{prefix}about">About</a></li><li><a href="{prefix}areas-we-serve">Areas</a></li><li><a href="{prefix}testimonials">Testimonials</a></li><li><a href="{prefix}faq">FAQ</a></li><li><a href="{prefix}contact">Contact</a></li></ul></div><div class="footer-col"><h4>Contact</h4><ul><li><a href="tel:{PHONE_RAW}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><button data-open-modal style="background:none;border:none;color:rgba(255,255,255,0.5);font-size:0.9rem;cursor:pointer;padding:0;">Free Estimate</button></li></ul></div></div><div class="footer-bottom"><span>&copy; 2026 Dre Home Services LLC</span><span><a href="{prefix}privacy" style="color:rgba(255,255,255,0.4);">Privacy</a> &middot; <a href="{prefix}terms" style="color:rgba(255,255,255,0.4);">Terms</a></span></div></div></footer>
<script src="{prefix}js/main.js"></script>
</body></html>
"""

def page_header(label, h1, p):
    return f"""
<header class="page-header"><div class="container"><span class="section-label">{label}</span><h1>{h1}</h1><p>{p}</p></div></header>
"""

def schema_service_json(name, desc, url, city="", schema_cat="HomeAndConstructionBusiness"):
    city_part = f'"areaServed": {{"@type": "City", "name": "{city}"}},' if city else ""
    return f"""<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "{schema_cat}", "name": "{name}", "description": "{desc}", "url": "{url}", "telephone": "{PHONE_RAW}", "email": "{EMAIL}", {city_part}"provider": {{"@type": "Organization", "name": "{COMPANY}", "logo": {{"@type": "ImageObject", "url": "{DOMAIN}/images/logo.png"}}}}, "image": "{DOMAIN}/images/og-image.png"}}</script>"""

# ============ SERVICE PAGES ============

def write_service_page(svc):
    slug = svc["slug"]
    path = f"{BASE}/services/{slug}"
    os.makedirs(path, exist_ok=True)

    title = f"{svc['name']} in Central Virginia | {COMPANY}"
    desc = f"{svc['description']} Free estimates across Fredericksburg, Stafford, Woodbridge & beyond. Call {PHONE}."
    canonical = f"{DOMAIN}/services/{slug}"
    keywords = svc["keywords"]

    # Build area links
    area_links = ""
    for city_slug, city_name, county, _, _, _, _ in cities:
        area_links += f'<a href="../areas/{city_slug}/{slug}" class="area-card"><h3>{city_name}</h3><p>{svc["short"]} services in {city_name}, {county}</p></a>\n'

    features_html = ""
    for feat in svc["features"]:
        features_html += f'<li style="color:var(--text-secondary);line-height:1.8;">{feat}</li>\n'

    html = head(title, desc, canonical, depth=1, keywords=keywords) + schema_service_json(svc["name"], desc, canonical, schema_cat=svc["schema_cat"]) + nav(prefix="../") + page_header(
        svc["short"],
        svc["headline"],
        f"Professional {svc['short'].lower()} services across Central Virginia. Licensed, insured, and locally trusted."
    ) + f"""
<section class="content-section"><div class="container">
<div class="reveal" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(min(100%, 520px), 1fr));gap:64px;align-items:center;">
  <div>
    <span class="section-label">What We Offer</span>
    <h2 style="text-align:left;" class="section-title">{svc['name']}</h2>
    <p style="color:var(--text-secondary);line-height:1.7;margin-bottom:20px;">{svc['description']}</p>
    <ul style="margin-bottom:20px;">
{features_html}
    </ul>
    <div style="display:flex;gap:12px;margin-top:28px;flex-wrap:wrap;"><button class="btn btn-primary" data-open-modal>Get a Free Quote</button><a href="tel:{PHONE_RAW}" class="btn btn-dark">Call {PHONE}</a></div>
  </div>
  <div class="service-card" style="padding:28px;">
    <h3 style="margin-bottom:16px;">Why Choose Dre Home Services</h3>
    <div style="display:flex;flex-direction:column;gap:14px;">
      <div style="display:flex;align-items:center;gap:10px;"><span style="color:var(--green-light);">&#10003;</span><span style="color:var(--text-secondary);font-size:0.9rem;">Licensed & insured professionals</span></div>
      <div style="display:flex;align-items:center;gap:10px;"><span style="color:var(--green-light);">&#10003;</span><span style="color:var(--text-secondary);font-size:0.9rem;">Free estimates on every project</span></div>
      <div style="display:flex;align-items:center;gap:10px;"><span style="color:var(--green-light);">&#10003;</span><span style="color:var(--text-secondary);font-size:0.9rem;">Same-day appointments available</span></div>
      <div style="display:flex;align-items:center;gap:10px;"><span style="color:var(--green-light);">&#10003;</span><span style="color:var(--text-secondary);font-size:0.9rem;">Upfront, no-surprise pricing</span></div>
      <div style="display:flex;align-items:center;gap:10px;"><span style="color:var(--green-light);">&#10003;</span><span style="color:var(--text-secondary);font-size:0.9rem;">Satisfaction guaranteed</span></div>
    </div>
  </div>
</div>
</div></section>

<section style="background:var(--bg-warm);"><div class="container">
<div class="section-header reveal"><span class="section-label">Areas We Serve</span><h2 class="section-title">{svc['name']} Near You</h2><p>Click your city below for localized service details and pricing.</p></div>
<div class="areas-grid reveal">
{area_links}
</div></div></section>

{cta_banner(prefix="../")}
{modal_overlay(prefix="../")}
{footer(prefix="../")}
"""
    with open(f"{path}/index.html", "w") as f:
        f.write(html)
    print(f"  services/{slug}/index.html written")

# ============ CITY + SERVICE COMBO PAGES ============

def write_city_service_page(city_data, svc):
    city_slug, city_name, county, d1, d2, d3, city_desc = city_data
    svc_slug = svc["slug"]
    svc_name = svc["name"]
    svc_short = svc["short"]

    path = f"{BASE}/areas/{city_slug}/{svc_slug}"
    os.makedirs(path, exist_ok=True)

    title = f"{svc_name} in {city_name}, {county} | {COMPANY}"
    desc = f"Professional {svc_name.lower()} in {city_name}, {county}. Free estimates, licensed & insured. Serving {d2} across {city_name}. Call {PHONE}."
    canonical = f"{DOMAIN}/areas/{city_slug}/{svc_slug}"
    keywords = f"{svc['keywords']}, {city_name.lower()} {svc_short.lower()}, {svc_short.lower()} {city_name.lower()} va, {svc_short.lower()} contractor {city_name.lower()}"

    # Other services in same city
    other_services = ""
    for other in services:
        if other["slug"] != svc_slug:
            other_services += f'<a href="../{other["slug"]}" class="service-card" style="text-align:left;padding:24px;"><h4 style="color:var(--brand-dark);margin-bottom:8px;">{other["name"]}</h4><p style="font-size:0.85rem;color:var(--text-secondary);">{other["short"]} services in {city_name}</p></a>\n'

    # Same service in other cities
    other_cities = ""
    for other_slug, other_city, other_county, _, _, _, _ in cities:
        if other_slug != city_slug:
            other_cities += f'<a href="../../{other_slug}/{svc_slug}" class="area-card"><h3>{other_city}</h3><p>{svc_short} in {other_city}</p></a>\n'

    features_html = ""
    for feat in svc["features"]:
        features_html += f'<li style="color:var(--text-secondary);line-height:1.8;">{feat}</li>\n'

    html = head(title, desc, canonical, depth=2, keywords=keywords) + schema_service_json(
        f"{svc_name} in {city_name}", desc, canonical, city=city_name, schema_cat=svc["schema_cat"]
    ) + nav(prefix="../../") + page_header(
        f"{city_name}, {county}",
        f"{svc_name} in {city_name}",
        f"Fast, professional {svc_short.lower()} services for {d2} in {city_name} and surrounding {county}."
    ) + f"""
<section class="content-section"><div class="container">
<div class="reveal" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(min(100%, 520px), 1fr));gap:64px;align-items:center;">
  <div>
    <span class="section-label">Local {svc_short}</span>
    <h2 style="text-align:left;" class="section-title">{svc_name} in {city_name}</h2>
    <p style="color:var(--text-secondary);line-height:1.7;margin-bottom:20px;">{COMPANY} proudly serves {city_name}, {d1}. We understand the unique needs of {d2} in this area — {city_desc} — and provide fast, reliable {svc_short.lower()} service with upfront pricing.</p>
    <p style="color:var(--text-secondary);line-height:1.7;margin-bottom:20px;">Whether you are maintaining {d3} or tackling a major renovation, our local crew arrives on time, handles all the heavy lifting, and leaves your property in better shape than we found it. Every job is backed by our satisfaction guarantee.</p>
    <ul style="margin-bottom:20px;">
{features_html}
    </ul>
    <div style="display:flex;gap:12px;margin-top:28px;flex-wrap:wrap;"><button class="btn btn-primary" data-open-modal>Get a Free Quote</button><a href="tel:{PHONE_RAW}" class="btn btn-dark">Call {PHONE}</a></div>
  </div>
  <div class="service-card" style="padding:28px;">
    <h3 style="margin-bottom:16px;">Why {city_name} Chooses Us</h3>
    <div style="display:flex;flex-direction:column;gap:14px;">
      <div style="display:flex;align-items:center;gap:10px;"><span style="color:var(--green-light);">&#10003;</span><span style="color:var(--text-secondary);font-size:0.9rem;">Same-day appointments available</span></div>
      <div style="display:flex;align-items:center;gap:10px;"><span style="color:var(--green-light);">&#10003;</span><span style="color:var(--text-secondary);font-size:0.9rem;">Upfront, no-surprise pricing</span></div>
      <div style="display:flex;align-items:center;gap:10px;"><span style="color:var(--green-light);">&#10003;</span><span style="color:var(--text-secondary);font-size:0.9rem;">Licensed & insured professionals</span></div>
      <div style="display:flex;align-items:center;gap:10px;"><span style="color:var(--green-light);">&#10003;</span><span style="color:var(--text-secondary);font-size:0.9rem;">Free estimates on every project</span></div>
      <div style="display:flex;align-items:center;gap:10px;"><span style="color:var(--green-light);">&#10003;</span><span style="color:var(--text-secondary);font-size:0.9rem;">Satisfaction guaranteed</span></div>
    </div>
  </div>
</div>
</div></section>

<section style="background:var(--bg-warm);"><div class="container">
<div class="section-header reveal"><span class="section-label">Other Services</span><h2 class="section-title">More Home Services in {city_name}</h2><p>We offer a full range of professional home improvement services across {county}.</p></div>
<div class="services-grid reveal" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr));">
{other_services}
</div></div></section>

<section class="content-section"><div class="container">
<div class="section-header reveal"><span class="section-label">Nearby Areas</span><h2 class="section-title">{svc_name} in Nearby Communities</h2></div>
<div class="areas-grid reveal">
{other_cities}
</div></div></section>

{cta_banner(prefix="../../")}
{modal_overlay(prefix="../../")}
{footer(prefix="../../")}
"""
    with open(f"{path}/index.html", "w") as f:
        f.write(html)
    print(f"  areas/{city_slug}/{svc_slug}/index.html written")

# ============ SITEMAP ============

def write_xml_sitemap():
    pages = [
        ("", "1.0", "weekly"),
        ("services/", "0.9", "monthly"),
        ("quote/", "0.9", "monthly"),
        ("about/", "0.8", "monthly"),
        ("contact/", "0.8", "monthly"),
        ("areas-we-serve/", "0.8", "monthly"),
        ("faq/", "0.7", "monthly"),
        ("testimonials/", "0.7", "monthly"),
        ("blog/", "0.8", "weekly"),
        ("privacy/", "0.3", "yearly"),
        ("terms/", "0.3", "yearly"),
        ("sitemap/", "0.3", "yearly"),
    ]
    # blog posts
    blog_posts = [
        "roof-cost-fredericksburg-2026",
        "roof-repair-signs-winter",
        "plumbing-emergency-before-plumber",
        "gutter-cleaning-frequency-virginia",
        "electrical-panel-upgrade-woodbridge",
        "power-washing-vs-pressure-washing",
        "deck-safety-inspection-caroline",
        "choose-licensed-contractor-virginia",
        "preventive-maintenance-checklist",
        "storm-damage-insurance-guide",
    ]
    for bp in blog_posts:
        pages.append((f"blog/{bp}/", "0.7", "yearly"))

    # city pages
    for slug, city, county, _, _, _, _ in cities:
        pages.append((f"areas/{slug}/", "0.8", "monthly"))

    # service pages
    for svc in services:
        pages.append((f"services/{svc['slug']}/", "0.8", "monthly"))

    # city+service combo pages
    for slug, city, county, _, _, _, _ in cities:
        for svc in services:
            pages.append((f"areas/{slug}/{svc['slug']}/", "0.7", "monthly"))

    urls = []
    for url, priority, changefreq in pages:
        urls.append(f"  <url><loc>{DOMAIN}/{url}</loc><priority>{priority}</priority><changefreq>{changefreq}</changefreq></url>")

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
""" + "\n".join(urls) + "\n</urlset>"

    with open(f"{BASE}/sitemap.xml", "w") as f:
        f.write(xml)
    print(f"\n  sitemap.xml written ({len(pages)} URLs)")

# ============ RUN ============

if __name__ == "__main__":
    print("Generating service pages...")
    for svc in services:
        write_service_page(svc)

    print("\nGenerating city+service combo pages...")
    total = len(cities) * len(services)
    count = 0
    for city_data in cities:
        for svc in services:
            write_city_service_page(city_data, svc)
            count += 1
            if count % 10 == 0:
                print(f"    ...{count}/{total}")

    print(f"\n  Done: {total} combo pages generated")

    print("\nGenerating sitemap.xml...")
    write_xml_sitemap()

    print("\n=== SUMMARY ===")
    print(f"Service pages:      {len(services)}")
    print(f"City pages:         {len(cities)}")
    print(f"City+Service pages: {len(cities) * len(services)}")
    print(f"Blog posts:         10")
    print(f"Support pages:      12")
    print(f"Total URLs:         {12 + len(cities) + len(services) + len(cities)*len(services) + 10}")
    print("All done.")
