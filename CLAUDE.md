# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Quick Start

**Zero build tools** — just serve the files with a local server and edit directly:

```bash
# Start a local server (pick one)
python -m http.server 8000          # Python 3
npx http-server                      # Node.js
python -m SimpleHTTPServer 8000     # Python 2
```

Visit `http://localhost:8000`, then open DevTools (F12) to debug. Changes to HTML/CSS/JS are visible on refresh.

**No install, no build step, no dependencies.**

## Project Overview

This is a modern, responsive personal portfolio website for Wayne Correa, a Cloud Infrastructure Product Leader. The site is built with vanilla HTML, CSS, and JavaScript—**no frameworks, no build tools, no dependencies**.

**Key stats:**
- 28+ years in product management
- $134M in combined revenue delivered
- Expertise: Cloud infrastructure, product strategy, enterprise leadership

## Technology Stack

- **HTML**: Semantic markup with Meta tags for SEO
- **CSS**: Custom CSS with CSS variables for theming, flexbox/grid layouts
- **JavaScript**: Vanilla JS (no frameworks) for interactivity
- **External**: Google Fonts (Inter, Outfit), Formspree for contact form backend
- **Hosting**: Static site suitable for any web host or CDN

## Architecture

**Single-page design** with 8 main sections (navigation links in index.html:19-25):
1. **Hero** — Stats cards with animated counter (script.js:49-82) + parallax gradient circle (script.js:164-180)
2. **About** — Text intro + sticky highlight box
3. **Achievements** — 6 cards in responsive grid, fade-in on scroll
4. **Expertise** — 4 skill categories with emoji headers
5. **Experience** — 6 timeline items with alternating left/right layout
6. **Contact** — Email/phone links (contact form removed; use Formspree for re-adds)
7. **Footer** — Simple copyright
8. **Sticky Navigation** — Updates active state dynamically based on scroll position

**Key interactivity** (all in script.js):
- Smooth anchor-link scrolling (lines 5-16)
- Fade-in animations via IntersectionObserver (lines 22-43; auto-unobserves for performance)
- Stats counter animation with format parsing (lines 49-82; detects $M, $B, %, +)
- Active nav highlighting (lines 135-160; 200px offset threshold)
- Parallax effect on hero gradient circle (lines 164-180; GPU-accelerated via transform)

**Design system** (CSS variables in styles.css:5-18):
- Colors: Primary blue (#0066ff), secondary orange (#ff6b35)
- Gradients: Two main ones (blue/orange) applied throughout
- Fonts: Inter (body), Outfit (headings) from Google Fonts
- Shadows: Three levels (sm, md, lg) for depth
- Spacing: 80px sections, responsive gaps (container padding 40px)
- Breakpoints: 768px (tablet), 480px (mobile)

## Customization for Job Opportunities

This portfolio is designed to be rapidly customized for different job opportunities using your resume files in the Job-Search directory. Here's the workflow:

### Typical Customization Flow (5-10 minutes)
1. **Identify the target role** and select the matching resume from `/home/wayne/AI-Projects/Job-Search/`
2. **Extract key metrics** from the resume:
   - Hero stats: Pick 4 strongest quantifiable results (28+ years, $1.4B, 200%, etc.)
   - Hero subtitle: Craft a 1-line hook emphasizing what the role cares about
   - Achievement cards: Select 6 examples that directly address job description keywords
   - Expertise order: Reorder 4 categories to match what the job posting emphasizes
3. **Update the portfolio** content (see "Quick Reference" table below for exact locations)
4. **Test locally** using local server:
   - Responsive design (test at 320px, 768px, 1440px widths)
   - All anchor links work and scroll smoothly
   - Animations trigger on scroll (stats counter, card fade-ins)
   - No console errors (F12)
5. **Deploy** to relevant portfolio URL/domain

### Quick Edits for Different Roles

**For Product Manager roles:**
- Update hero subtitle (index.html:33) to emphasize product strategy focus
- Reorder achievement cards (index.html:83-118) to highlight product launches first
- Adjust expertise section (index.html:128-167) to emphasize "Product & Strategy"
- Update 4 hero stats (index.html:35-50) to show product-relevant metrics

**For Leadership/Sales roles:**
- Emphasize revenue delivery in hero stats (index.html:35-50)
- Move "Enterprise Sales Excellence" achievement card to top
- Highlight "Leadership & Sales" expertise category
- Update stats to show leadership-relevant metrics

**For Cloud/Infrastructure roles:**
- Focus hero on technical infrastructure achievements
- Lead with "Cloud & Infrastructure" expertise category (index.html:128-137)
- Highlight Equinix and IBM Direct Link experiences in timeline
- Update stats to show infrastructure-relevant metrics

### Content Mapping from Resumes
- **Hero stats** (index.html:35-50): Pull 4 strongest metrics from resume (displayed in single row on desktop, wraps on mobile)
- **Achievement cards** (index.html:83-118): 6 best examples from your experience, ordered by relevance to role
- **Expertise sections** (index.html:128-167): Match 4 categories to job description keywords
- **Timeline** (index.html:177-237): Keep all entries, let achievement cards emphasize relevance

### SEO & Meta Tags
When customizing for different roles, update these meta tags for better search visibility and social sharing (index.html:6-7):
- **Description** (`<meta name="description">`): Keep under 160 characters; include role, years of experience, and key metrics
- **Keywords** (`<meta name="keywords">`): Comma-separated list matching job description keywords (e.g., "Product Manager, SaaS, B2B")
- **Page Title** (`<title>`): Use format "Name | Role Specialization" for better SEO
- **Example**: For a Cloud Platform PM role, update to: "Wayne Correa | Cloud Platform Product Manager"

## Development Workflow

**Testing**: Start local server (see Quick Start), open DevTools (F12), toggle device toolbar (Ctrl+Shift+M) for responsive testing. Check console for errors. Test across Chrome, Firefox, Safari, Edge (ES6+ required).

**Content edits for role customization** (see Quick Reference table below):
- Hero subtitle (index.html:33)
- Hero stats 4 cards (index.html:35-50) — must use format: `$1.4B`, `28+`, `200%`, etc.
- Achievement cards reorder (index.html:83-118)
- Expertise categories reorder (index.html:128-167)
- Timeline items (index.html:177-237) — keep chronological

**Theming**: Edit CSS variables in styles.css:5-18 (primary/secondary colors cascade to all gradients and shadows). Responsive design mobile-first; media queries at 768px and 480px in styles.css:724-819. Font imports in index.html:10-12.

**Contact section**: Email/phone/LinkedIn links in index.html:285-296. Form removed; to re-add: use Formspree endpoint `https://formspree.io/f/myzopbzd` and update script.js.

## Quick Reference: Edit Locations

Quick lookup for the most common edits when customizing for different roles:

| Content | File | Lines | Notes |
|---------|------|-------|-------|
| Hero subtitle (first impression) | index.html | 33 | Update to match role focus |
| Hero stats (4 key metrics) | index.html | 35-50 | Pull from resume; 4 stat cards displayed |
| Achievement cards | index.html | 83-118 | 6 cards total; reorder by relevance |
| Cloud & Infrastructure skills | index.html | 128-137 | First expertise category |
| Product & Strategy skills | index.html | 139-147 | Second expertise category |
| Leadership & Sales skills | index.html | 149-157 | Third expertise category |
| Certifications & Learning | index.html | 159-167 | Fourth expertise category |
| Timeline items (experience) | index.html | 177-237 | 5 entries total; order is chronological |
| Color scheme (CSS variables) | styles.css | 5-18 | Primary (#0066ff), secondary (#ff6b35) |
| Responsive breakpoints | styles.css | 724-819 | 768px (tablet), 480px (mobile) |
| Stats counter animation | script.js | 49-82 | Detects $M, B, %, or + formatting |
| Active nav highlighting | script.js | 135-160 | Updates on scroll (200px offset) |

## File Structure

```
waynecorrea/
├── index.html          # Main HTML file with all content (299 lines)
├── styles.css          # All styling (756 lines, well-commented)
├── script.js           # Client-side interactivity (191 lines)
├── CNAME               # Custom domain configuration
└── CLAUDE.md           # This file

Related directory:
../Job-Search/         # Resume files for different opportunities
├── Wayne Correa - MGMTinMotion.pdf
├── Wayne Correa Resume - Flexential.docx
├── Wayne Correa Resume GCP PM.pdf
└── [other role-specific resumes]
```

## Performance Notes

- No build process or dependencies to install
- CSS custom properties enable efficient theme changes
- IntersectionObserver used efficiently for scroll animations (auto-unobserves when done)
- Parallax effect uses `transform` property (GPU-accelerated)
- Contact form offloads backend to Formspree (zero-cost for non-commercial use)

## Key Implementation Details

**Stats Counter** (script.js:49-82): Parses text to detect format ($M, $B, %, +). Animates over 30 steps at 50ms intervals. Format validation is strict—ensure values match regex `/[\d.]+/` with suffix attached.

**Timeline Layout** (styles.css:476-482): Alternates left/right via `direction: rtl` on even items. Maintains visual balance; don't remove this CSS rule.

**Active Nav Highlighting** (script.js:135-160): Uses 200px scroll offset threshold. Adds `active` class to current link dynamically. Links update as user scrolls.

**Scroll Animations** (script.js:22-43): IntersectionObserver with threshold 0.1 (triggers when 10% visible). **Critical**: `observer.unobserve()` prevents re-polling after animation fires. Don't remove—performance depends on it. Elements fade-in once, not on every scroll.

**Parallax Effect** (script.js:164-180): GPU-accelerated via `transform: translateY()`. Multiply factor controls intensity. Subtle effect is intentional (aggressive parallax causes motion sickness).

**Job-Search alignment** (when customizing): Review `/home/wayne/AI-Projects/Job-Search/` resumes first. Extract 4 strongest stats, 6 relevant achievements, reorder expertise to match job description keywords.

## Known Limitations & Troubleshooting

**Limitations**:
- No bundling/minification (single script.js file; keep under 10KB)
- Google Fonts requires internet (gracefully degrades to system fonts)
- Formspree contact form requires internet; not suitable for fully offline use
- No dark mode toggle (would require runtime CSS swapping)
- No asset versioning — users must hard-refresh (Ctrl+Shift+R) for CSS/JS changes
- Mobile navigation always visible (hamburger menu would need extra JS)
- Stats counter limited to 4 visible cards (responsive grid constraint)

**Troubleshooting**:
- **Animations not firing**: IntersectionObserver requires scroll to trigger (not on page load). Test in DevTools device toolbar. Supported in all modern browsers (IE11+ with polyfill).
- **Stats counter not animating**: Check format strictness — must be `$1.4B`, `28+`, `200%`, etc. Missing $ or text suffix breaks parser.
- **Google Fonts not loading**: Requires HTTPS or localhost. Falls back to system fonts (acceptable). For offline: download Inter/Outfit and update index.html:10-12.
- **Responsive issues**: Test at 480px, 768px, 1440px (DevTools device toolbar). Mobile-first CSS in styles.css:724-819. Test on real devices if possible.
- **Browser compatibility**: Chrome, Firefox, Safari, Edge (ES6+ required). IE11 not supported. JS failures don't break HTML structure.

## Deployment

**Any static host works** (GitHub Pages, Netlify, Vercel): just upload all files. No env vars, no build step, no secrets. HTTPS required for Google Fonts.

**GitHub Pages (current setup)**:
- `CNAME` file points to `waynecorrea.com`
- DNS: A records at registrar point to GitHub servers (185.199.108.153, etc.)
- Deploy: Push to `master` branch → auto-deploys in ~1 minute
- Settings → Pages must be set to deploy from `master` branch
- HTTPS auto-provisioned

**Switching to Netlify/Vercel**: Delete `CNAME` file (GitHub-specific), connect repo, select deploy branch. They auto-detect static HTML and provision HTTPS.
