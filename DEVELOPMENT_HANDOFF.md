# WireHarness_Global_V1 Development Handoff

This document summarizes the current state of the Wire Harness Equipment Global Site V1 project so another GPT/Codex session can review it and propose the next step without guessing.

## 1. Project Goal

Project name: Wire Harness Equipment Global Site V1

Primary business goal: get the first overseas WhatsApp inquiry for wire processing equipment.

Technical direction:
- Static HTML website only.
- No backend.
- No database.
- No login.
- No CDN dependency.
- Dark industrial style with orange primary color.
- Mobile responsive.

Main conversion action:
- WhatsApp inquiry.
- Unified WhatsApp URL:

```text
https://wa.me/8618066282233?text=Hello%2C%20I%20need%20information%20about%20your%20wire%20processing%20equipment
```

## 2. Placeholder Rules

Do not replace placeholders until real launch information is confirmed.

Current placeholders:
- `wirexatech.com`
- `8618066282233`
- `WIREXA TECH`
- `WhatsApp support available`

Launch URLs are unified under `https://wirexatech.com/`.

## 3. Current File Structure

Root directory:

```text
C:\Users\Administrator\Documents\网站小程序\WireHarness_Global_V1
```

Current root files:
- 23 HTML pages
- 1 sitemap file
- 1 robots file
- 1 handoff document

Directories:
- `assets/`
- `images/`

## 4. Current HTML Pages

Core pages:
- `index.html`
- `products.html`
- `contact.html`

Product pages:
- `product-wire-stripping-machine.html`
- `product-terminal-crimping-machine.html`
- `product-808-series.html`
- `product-806cn-wire-stripping-twisting-machine.html`
- `product-880-series.html`

Fault articles:
- `fault-feeding-error.html`
- `fault-blade-replacement.html`
- `fault-stripping-length.html`
- `fault-wire-damage.html`
- `fault-length-inconsistent.html`

Guide articles:
- `guide-how-to-choose.html`
- `guide-automatic-vs-manual.html`
- `guide-ev-harness.html`
- `guide-blade-selection.html`

Case page:
- `cases.html`

Selector tool:
- `selector.html`

Multilingual pages:
- `index-ru.html`
- `index-pt.html`
- `contact-ru.html`
- `contact-pt.html`

SEO/support files:
- `sitemap.xml`
- `robots.txt`

## 5. Product System Status

Current product entry logic:

```text
Any page navigation "Products"
  -> products.html
     -> product-wire-stripping-machine.html
     -> product-terminal-crimping-machine.html
     -> product-808-series.html
     -> product-806cn-wire-stripping-twisting-machine.html
     -> product-880-series.html
```

`products.html` now displays 5 product cards:
- Automatic Computer Wire Stripping Machine
- Servo Terminal Crimping Machine (FY-4T)
- FY-808 Series Automatic Wire Stripping Machine
- 806CN Wire Stripping & Twisting Machine
- FY-880 Series Heavy Wire Stripping Machine

The existing generic stripping machine page has been updated with 808-style parameters:
- Wire size: 0.1-6mm², AWG30-12
- Cutting length: 0.1-99999.9mm programmable
- Front stripping: 0.1-25mm
- Rear stripping: 0.1-70mm
- Middle stripping: 16 segments
- Speed reference: approx. 4550 / 4300 / 3000 / 2000 pcs per hour at 50 / 100 / 500 / 1000mm
- Power: AC220V, 50/60Hz, approx. 680W
- Display: 4.3-inch touchscreen
- Weight: approx. 31.5kg
- Dimensions: 470mm x 450mm x 350mm

Independent model pages summarize:
- 808 / 808S compact automatic stripping series
- 806CN stripping and wire-end twisting machine
- 880A / 880B / 880C / 880D heavy wire and multi-core cable series

## 6. Image Assets

Current website-ready product images:
- `images/product-main.jpg`
- `images/product-detail.jpg`
- `images/product-crimping.jpg`
- `images/product-808-series.jpg`
- `images/product-806cn.jpg`
- `images/product-880a.jpg`
- `images/product-880b.jpg`
- `images/product-880c.jpg`

Original/source images still present:
- `images/4T.png`
- `images/806CN新款1.png`
- `images/外贸款-816-1.png`

Do not delete original images unless explicitly requested.

## 7. Design Conventions

Current style direction:
- Industrial dark background.
- Main background: `#1a1a1a`
- Main orange: `#ff6600`
- Deep gray cards.
- Orange CTA buttons.
- Fixed bottom-right WhatsApp floating button.
- Product cards use dark panels, top image, short description, orange-outline pill tags, and a `View Details ->` CTA.

Important layout note:
- Floating WhatsApp button previously overlapped product card tags.
- This was fixed in `products.html` by reducing floating button size and spacing.
- Future page additions should check floating button overlap on desktop and mobile.

## 8. Navigation Status

Main navigation should be:

```text
Products -> products.html
Fault Solutions -> fault-feeding-error.html
Cases -> cases.html
Contact -> contact.html
Free Consultation -> WhatsApp link
```

Multilingual index/contact pages also point product navigation to `products.html`.

## 9. Current Verification Status

Browser checks already completed locally:
- `products.html` renders correctly on desktop.
- `products.html` renders correctly at 390px mobile width.
- 5 product cards display correctly.
- Product card images load successfully.
- No visible broken images in checked product pages.
- Floating WhatsApp button does not overlap visible product tags/buttons.
- New model pages open successfully.
- New model pages contain title, description, canonical, parameter tables, and WhatsApp CTAs.

Git note:
- The current PowerShell environment did not have `git` available, so no git diff/stat was produced.

## 10. Known Gaps Before Launch

Business/contact setup:
- Replace domain placeholder.
- Replace WhatsApp phone placeholder.
- Replace company name placeholder.
- Replace email placeholder.

SEO setup:
- Ensure every canonical URL uses the final domain.
- Ensure `sitemap.xml` uses the final domain consistently.
- Submit sitemap to Google Search Console.
- Add Google Analytics or another lightweight tracking method if desired.
- Consider adding basic product schema/FAQ schema later.

Content gaps:
- Russian and Portuguese versions only exist for home and contact pages.
- Product pages and articles are currently English only.
- YouTube iframe placeholders are still empty.
- Some model parameters were extracted from Word documents; final factory review is recommended before publishing.

Operational gaps:
- No public domain deployment completed yet.
- No Search Console verification completed yet.
- WhatsApp click tracking is still manual unless tracking is added.

## 11. Recommended Next Development Steps

Priority 1: Launch readiness
- Replace placeholders globally after real domain, WhatsApp number, company name, and email are confirmed.
- Re-run full link/image checks.
- Deploy static site to hosting.
- Submit sitemap to Google Search Console.

Priority 2: Conversion improvement
- Add stronger CTA blocks on product model pages.
- Add "Send wire photo" messaging to model pages.
- Add downloadable spec table or PDF later if needed.
- Add WhatsApp click tracking if analytics is installed.

Priority 3: SEO content expansion
- Add one comparison guide: `808 vs 806CN vs 880 Series - Which Wire Stripping Machine Do You Need?`
- Add one application page: automotive harness production.
- Add one troubleshooting hub page linking all fault articles.
- Add FAQ blocks to product pages.

Priority 4: Multilingual expansion
- Translate product center and key product pages into Russian and Portuguese if overseas traffic confirms demand.

## 12. Safe Rules For The Next GPT/Codex Session

When continuing this project:
- Do not redesign the whole website unless explicitly requested.
- Keep the dark industrial/orange style.
- Keep static HTML only.
- Keep all WhatsApp links using the unified placeholder format until launch info is provided.
- Do not remove existing pages.
- Do not overwrite source/original images unless explicitly requested.
- Do not invent machine parameters. If unsure, mark as "to confirm".
- Before publishing, run desktop and mobile browser checks.

## 13. Copy-Paste Prompt For GPT

Use this prompt to ask GPT for suggestions:

```text
You are reviewing a static industrial equipment website project for overseas lead generation.

Project: Wire Harness Equipment Global Site V1
Goal: get the first overseas WhatsApp inquiry.
Technical scope: pure static HTML, no backend, no database, no CDN.
Style: dark industrial background (#1a1a1a), orange primary color (#ff6600), mobile responsive.

Current site includes:
- Home page
- Product center
- Generic wire stripping product page
- Terminal crimping product page
- Independent model pages for 808 / 806CN / 880 series
- 5 troubleshooting articles
- 4 buying guide/application articles
- 3 case studies
- 60-second machine selector
- Contact page
- Russian/Portuguese home and contact pages
- sitemap.xml and robots.txt

Current placeholders:
- wirexatech.com
- 8618066282233
- WIREXA TECH
- WhatsApp support available

Please review the current project direction and propose the next highest-ROI actions before launch.
Focus on:
1. WhatsApp inquiry conversion
2. Google indexing and SEO
3. Product page trust and clarity
4. Minimal static-site implementation
5. Avoiding unnecessary V2 features

Output:
- Top 10 recommended improvements
- Which 3 should be done before launch
- Exact Codex instructions for the next implementation step
- Any risks or checks before publishing
```

## 14. Suggested Next Codex Instruction

If real launch information is ready, use this:

```text
In WireHarness_Global_V1, replace all placeholders globally:
- wirexatech.com -> [real domain]
- 8618066282233 -> [real WhatsApp number, digits only with country code]
- WIREXA TECH -> [real company name]
- WhatsApp support available -> [real email]

Also normalize sitemap.xml and all canonical URLs to the real domain.

Safety limits:
- Only replace placeholders and canonical/sitemap domain values.
- Do not change layout, design, product parameters, or page content.
- After replacement, run local browser checks for index.html, products.html, product-wire-stripping-machine.html, contact.html, and sitemap.xml.
- Output the modified file list and any remaining placeholders.
```
