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
- **Contact form** - Uses Formspree API (myzopbzd) to send emails to waynejcorrea@gmail.com

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
   - Hero stats: Pick 3 strongest quantifiable results (28+ years, $134M, 347% growth, etc.)
   - Hero subtitle: Craft a 1-line hook emphasizing what the role cares about
   - Achievement cards: Select 6 examples that directly address job description keywords
   - Expertise order: Reorder 4 categories to match what the job posting emphasizes
3. **Update the portfolio** content (see "Quick Reference" table below for exact locations)
4. **Test locally** using local server:
   - Responsive design (test at 320px, 768px, 1440px widths)
   - All anchor links work
   - Contact form submits successfully
   - No console errors (F12)
5. **Deploy** to relevant portfolio URL/domain

### Quick Edits for Different Roles

**For Product Manager roles:**
- Update hero subtitle (index.html:33) to emphasize product strategy focus
- Reorder achievement cards (index.html:83-118) to highlight product launches first
- Adjust expertise section (index.html:128-167) to emphasize "Product & Strategy"

**For Leadership/Sales roles:**
- Emphasize revenue delivery in hero stats (index.html:35-46)
- Move "Enterprise Sales Excellence" achievement card to top
- Highlight "Leadership & Sales" expertise category

**For Cloud/Infrastructure roles:**
- Focus hero on technical infrastructure achievements
- Lead with "Cloud & Infrastructure" expertise category (index.html:128-137)
- Highlight Equinix and IBM Direct Link experiences in timeline

### Content Mapping from Resumes
- **Hero stats** (index.html:35-46): Pull 3 strongest metrics from resume
- **Achievement cards** (index.html:83-118): 6 best examples from your experience, ordered by relevance to role
- **Expertise sections** (index.html:128-167): Match 4 categories to job description keywords
- **Timeline** (index.html:177-237): Keep all entries, let achievement cards emphasize relevance

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

### Contact Form Configuration
- **Current endpoint**: `https://formspree.io/f/myzopbzd` (script.js:68)
- **Recipient email**: waynejcorrea@gmail.com
- **To change recipient**:
  1. Go to formspree.io and create a new form
  2. Update the endpoint URL in script.js:68
  3. Test by submitting the form
- **Form validation**: HTML5 `required` attributes handle validation
- **Fallback**: If Formspree is down, error handler shows fallback email

## Quick Reference: Edit Locations

Quick lookup for the most common edits when customizing for different roles:

| Content | File | Lines | Notes |
|---------|------|-------|-------|
| Hero subtitle (first impression) | index.html | 33 | Update to match role focus |
| Hero stats (3 key metrics) | index.html | 35-46 | Pull from resume |
| Achievement cards | index.html | 83-118 | 6 cards total; reorder by relevance |
| Cloud & Infrastructure skills | index.html | 128-137 | First expertise category |
| Product & Strategy skills | index.html | 139-147 | Second expertise category |
| Leadership & Sales skills | index.html | 149-157 | Third expertise category |
| Certifications & Learning | index.html | 159-167 | Fourth expertise category |
| Timeline items (experience) | index.html | 177-237 | 5 entries total; order is chronological |
| Color scheme (CSS variables) | styles.css | 5-18 | Primary (#0066ff), secondary (#ff6b35) |
| Responsive breakpoints | styles.css | 724-819 | 768px (tablet), 480px (mobile) |
| Contact form API endpoint | script.js | 68 | Formspree form ID |
| Stats counter animation | script.js | 101-135 | Detects $M, %, or + formatting |
| Active nav highlighting | script.js | 190-208 | Updates on scroll (200px offset) |

## File Structure

```
waynecorrea/
├── index.html          # Main HTML file with all content
├── styles.css          # All styling (800+ lines, well-commented)
├── script.js           # Client-side interactivity (245 lines)
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

### Form Submission (script.js:53-94)
The form uses async fetch to Formspree. Error handling provides fallback email address (waynejcorrea@gmail.com). Status messages display for 5 seconds on success.

### Active Nav Link (script.js:190-208)
Detects current section based on scroll position with 200px offset. Links update dynamically. The active state adds `active` class which triggers the underline (defined in CSS but not currently visible—could be styled further).

## Troubleshooting

### Form Submission Not Working
- **Check Formspree status**: Visit formspree.io to verify the form exists and is active
- **Check endpoint**: Verify the URL in script.js:68 matches the one from Formspree dashboard
- **Check browser console**: Look for CORS errors or network failures (F12 → Console tab)
- **Fallback behavior**: If Formspree fails, error message shows `waynejcorrea@gmail.com` for manual contact
- **Test locally**: Formspree may reject localhost requests — test on deployed domain instead

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
- **Check format**: Counter only animates values with $M (millions), % (percent), or + (count) suffix
- **Example formats**:
  - ✅ `$134M` (revenue)
  - ✅ `28+` (count)
  - ✅ `347%` (percentage)
  - ❌ `134M` (missing $)
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

- Deploy entire directory as-is to any static hosting (GitHub Pages, Netlify, Vercel, etc.)
- No environment variables or secrets needed (Formspree form ID is public)
- Works offline except for Google Fonts and Formspree
- All modern browsers supported (uses ES6+ JavaScript features)
