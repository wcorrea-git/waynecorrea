# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Quick Start

**This is a zero-build-tools project** — just open `index.html` in a browser or use a local server:
```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000

# Node.js
npx http-server
```
Then visit `http://localhost:8000` and open your DevTools (F12) to inspect/debug.

**No install needed.** Edit the HTML, CSS, or JS files directly and refresh your browser to see changes.

## Commands

This project has **zero build tools** — no npm scripts, no build process, no compilation needed. Everything runs directly in the browser:

```bash
# Start a local development server (pick one)
python -m http.server 8000          # Python 3
npx http-server                      # Node.js
python -m SimpleHTTPServer 8000     # Python 2 (legacy)
```

Then navigate to `http://localhost:8000` in your browser. Changes to HTML/CSS/JS are immediately visible on refresh.

**No other commands needed** — this is a static site with no dependencies to install, lint, test, or build.

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

## Architecture & Key Components

### Page Structure
The site uses a single-page application (SPA) design with smooth scrolling:
1. **Navigation (sticky navbar)** - Links to all sections with active state highlighting
2. **Hero Section** - Eye-catching intro with stats cards and CTAs
3. **About** - Personal introduction with sticky highlight box
4. **Achievements** - 6 achievement cards in responsive grid
5. **Expertise** - 4 categories of skills with checkmark styling
6. **Experience** - Timeline layout (alternating left/right on desktop)
7. **Contact** - Gradient background with contact info + contact form
8. **Footer** - Simple footer with copyright

### Key JavaScript Behaviors
- **Smooth scrolling** - Anchor links scroll smoothly to sections
- **Scroll animations** - Elements fade in as they enter viewport (IntersectionObserver)
- **Active nav highlighting** - Highlights current section in navigation based on scroll position
- **Stats counter animation** - Numbers animate upward when hero section is visible
- **Parallax effect** - Subtle parallax on gradient circle in hero
- **Navbar scroll effect** - Shadow changes on scroll
- **Contact form** - Uses Formspree API (myzopbzd) to send emails to email@waynecorrea.com

### CSS Design System
- **Color scheme**: Primary blue (#0066ff), secondary orange (#ff6b35), light gray backgrounds
- **Gradients**: Two main gradients (blue and orange) used throughout
- **Typography**: Inter (body), Outfit (headings) from Google Fonts
- **Shadows**: Three levels (sm, md, lg) for depth
- **Spacing**: Consistent 80px section padding, responsive gaps
- **Responsive breakpoints**: 768px (tablet), 480px (mobile)

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

### Local Testing
1. **Start a local server** (see Quick Start above)
2. **Open DevTools** with F12 to inspect elements and debug
3. **Test responsive design** — DevTools → toggle device toolbar (Ctrl+Shift+M / Cmd+Shift+M)
4. **Check console** for any JavaScript errors
5. **Test form submission** — fill out contact form and verify email arrives
6. **Test all browsers** — Chrome, Firefox, Safari, Edge (uses ES6+ features)

### Content Updates (for Job Customization)
1. **Update hero subtitle** (`index.html:33`) — this is the first impression
2. **Update hero stats** (`.stat-card` in `index.html:35-46`) — pull 3 metrics from resume
3. **Reorder achievement cards** (`.achievement-card` in `index.html:83-118`) — put most relevant first
4. **Reorder expertise categories** (`.expertise-category` in `index.html:128-167`) — match job description keywords
5. **Add/update timeline** (`.timeline-item` in `index.html:177-237`) — keep chronological order

### Styling & Theme Changes
- **Global colors**: Update CSS variables in `:root` (styles.css:5-18)
  - `--primary-color` (#0066ff) — main brand blue
  - `--secondary-color` (#ff6b35) — accent orange
  - All other colors cascade from these two
- **Responsive design**: Mobile-first approach
  - Base styles apply to all screens
  - Media queries at 768px (tablet) and 480px (mobile)
  - Adjust in styles.css:724-819
- **Typography**: Change font imports in index.html:10-12 if needed

### Contact Section
- **Contact info**: Name, email, and links in footer section (index.html:238+)
- **Email**: email@waynecorrea.com
- **Note**: Direct contact form submission has been removed in favor of displaying contact information and email link
- **If you want to re-add a contact form**:
  1. The old Formspree endpoint was `https://formspree.io/f/myzopbzd`
  2. Add a form element in the contact section
  3. Update script.js to handle form submission
  4. Test with a real email address before deployment

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

## Important Implementation Details

### Syncing with Job-Search Resumes
The portfolio content should align with your resume files in `/home/wayne/AI-Projects/Job-Search/`. Key alignment points:
- **Hero stats**: Extract 3 strongest quantifiable results from the target resume
- **Achievement cards**: Pull 6 best examples that match the job description
- **Expertise sections**: Reorder or emphasize categories matching job requirements
- When tailoring for a specific opportunity, review the corresponding resume first to ensure consistency

### Stats Counter (script.js:101-135)
The counter animation parses text content to detect format (currency with $M, percentage %, or count with +). Ensure stat values maintain this format when updating.

### Timeline Alternation (styles.css:476-482)
The experience timeline alternates left/right using CSS `direction: rtl` on even items. This creates the classic alternating timeline look. Maintain this pattern when adding new experiences.

### Active Nav Link (script.js:135-160)
Detects current section based on scroll position with 200px offset. Links update dynamically. The active state adds `active` class which triggers the underline (defined in CSS but not currently visible—could be styled further).

### IntersectionObserver Cleanup (script.js:27-43)
The scroll animations use IntersectionObserver with automatic cleanup via `observer.unobserve()` after each element animates in. This is critical for performance:
- **Why it matters**: Without cleanup, the observer would keep polling all elements, wasting CPU cycles
- **How it works**: Each element fades in once, then gets unwatched — subsequent scrolls don't re-trigger animations
- **Modifying it**: If you want elements to animate on every scroll (not recommended), remove the `observer.unobserve()` call but expect performance impact
- **Threshold of 0.1**: Elements animate when 10% of their area is visible; adjust `threshold: 0.1` in observerOptions to change this behavior

### Parallax Effect (script.js:164-180)
The hero section includes a subtle parallax effect on the gradient circle background element. It uses `requestAnimationFrame` for smooth 60fps updates:
- **Performance**: Uses `transform: translateY()` (GPU-accelerated) not `top/position` properties
- **Customization**: Multiply factor in line ~172 controls intensity (higher = more dramatic parallax)
- **Why not more visible**: Subtle parallax is professional; aggressive parallax can cause motion sickness

## Known Limitations

- **No JavaScript bundling/minification**: All JS runs in a single file without tree-shaking. Good for small sites, but keep script.js under 10KB
- **No offline fonts**: Google Fonts requires internet connection; site gracefully degrades to system fonts but loses design polish
- **No form backend without Formspree**: Contact form submission requires Formspree service (requires internet, not suitable for fully offline use)
- **No dark mode toggle**: CSS variables are set at build time in `:root`. Adding dark mode would require JavaScript to swap themes dynamically
- **No real-time notifications**: No build process means no asset versioning. Users must hard-refresh (Ctrl+Shift+R) to see CSS/JS changes
- **Mobile menu not implemented**: Navigation is always visible (hamburger menu would need additional JS). Works fine on mobile but takes vertical space
- **Stats counter limited to 4 visible cards**: Responsive design limits to 2x2 grid on tablet; adding more stats requires layout redesign

## Troubleshooting

### Google Fonts Not Loading
- **Check internet connection**: Fonts are loaded from fonts.googleapis.com (requires HTTPS or localhost)
- **Fallback fonts**: If Google Fonts fails, system defaults to serif/sans-serif (acceptable but less polished)
- **Test offline**: Run locally without internet — fonts will not load, but site remains functional
- **Self-host fonts**: Download Inter and Outfit fonts and replace links in index.html:10-12 for offline version

### Animations Not Triggering
- **Check IntersectionObserver support**: Supported in all modern browsers (IE11+ with polyfill)
- **Check scroll position**: Animations fire when elements enter viewport (not when page first loads)
- **Disable for testing**: Set opacity to 1 in styles.css:210 to verify animations aren't blocking visibility

### Stats Counter Not Animating
- **Check format**: Counter animates values with $M (millions), $B (billions), % (percent), or + (count) suffix
- **Example formats**:
  - ✅ `$1.4B` (revenue in billions)
  - ✅ `28+` (count)
  - ✅ `200%` (percentage)
  - ✅ `10+` (year count)
  - ❌ `1.4B` (missing $)
  - ❌ `28 years` (text suffix breaks parser)

### Responsive Design Issues
- **Test breakpoints**: Use DevTools device toolbar at 480px, 768px, 1440px
- **Check media queries**: Mobile-first breakpoints in styles.css:724-819
- **Test on real devices**: iPhone, iPad, Android phones may render differently than DevTools simulation
- **Clear cache**: Hard refresh (Ctrl+Shift+R / Cmd+Shift+R) to bypass browser cache

### Browser Compatibility
- **Supported**: Chrome, Firefox, Safari, Edge (all modern versions)
- **Not supported**: IE11 and older (ES6+ JavaScript not compatible)
- **Graceful degradation**: If JavaScript fails, basic structure still visible

## Deployment

### Quick Deploy Options

**Any static hosting works** (GitHub Pages, Netlify, Vercel, etc.) — just upload all files as-is:

- No environment variables or secrets needed (Formspree form ID is public)
- No build step required
- Works offline except for Google Fonts and Formspree CDN
- All modern browsers supported (uses ES6+ JavaScript features)

### GitHub Pages (waynecorrea.com)

The `CNAME` file is configured for GitHub Pages with custom domain:

1. **Custom domain setup**: `CNAME` file points to `waynecorrea.com`
2. **DNS configuration**: Domain registrar must have A records pointing to GitHub's servers (185.199.108.153, etc.)
3. **HTTPS**: GitHub Pages automatically provisions SSL certificate (required for Google Fonts)
4. **Deployment**: Push changes to `master` branch → GitHub Pages auto-deploys in ~1 minute
5. **Branch requirement**: Ensure GitHub Pages is set to deploy from `master` branch (check repo Settings → Pages)

### Netlify/Vercel (Alternative)

If switching away from GitHub Pages:
1. Delete the `CNAME` file (GitHub Pages-specific)
2. Connect repo to Netlify/Vercel and select deploy branch
3. No configuration needed — they auto-detect static HTML
4. Environment: These services also provide HTTPS automatically
