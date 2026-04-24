# Repository Guidelines

## Project Structure & Module Organization
- `site.config.json`: Site-wide metadata and shared navigation data.
- `tools/build_site.py`: Local no-dependency build script for generated journal pages and sitemap updates.
- `posts/*.md`: Source of truth for journal content.
- `index.html`, `post.html`, `posts/*.html`, `sitemap.xml`: Generated output for the journal experience.
- `about.html`, `projects.html`: Hand-authored static pages with build-time injected nav dropdown content.
- `styles.css`: Global styles, CSS variables, and responsive rules.
- `script.js`: Vanilla JS behavior (navigation, theme, UI interactions).
- `posts/`: Markdown source plus post assets (for example, `posts/the-augmented-product-manager.md`).
- `screen.png`: Static asset used in the site.
- `CNAME`: Custom domain for GitHub Pages.

## Build, Test, and Development Commands
- Build generated pages locally with `python tools/build_site.py`.
- Local preview:
  - `python -m http.server 8000` (Python 3)
  - `npx http-server` (Node, if installed)
- Open `http://localhost:8000` and refresh to see changes.

## Coding Style & Naming Conventions
- Indentation: 4 spaces in HTML/CSS/JS.
- HTML: semantic structure, descriptive class names (for example, `.site-header`, `.nav-menu`).
- CSS: use variables in `:root` for colors and spacing; keep component blocks grouped.
- JS: vanilla, minimal DOM queries, prefer `const` and early returns for readability.

## Testing Guidelines
- No automated test framework in this repo.
- Manual checks before changes:
  - Run `python tools/build_site.py` and confirm it completes without errors.
  - Desktop and mobile widths (320px, 768px, 1440px).
  - Navigation, dropdowns, and theme toggle.
  - Journal index, latest post, and generated `posts/*.html` links.
  - Console free of errors.

## Commit & Pull Request Guidelines
- Commit messages generally follow Conventional Commits: `feat: ...`, `fix: ...`, `chore: ...`.
- Keep commits scoped to one change area when possible.
- PRs should include:
  - Clear description of what changed and why.
  - Screenshots for visual changes.
  - Linked issue or context if applicable.

## Configuration & Deployment Notes
- Hosted on GitHub Pages; custom domain is defined in `CNAME`.
- External dependencies: Google Fonts and Feather Icons via CDN.
- Deployment is still Git-based static hosting. The required local workflow is: edit source files, run `python tools/build_site.py`, preview locally, then commit and push the generated static files.
- Prefer editing `posts/*.md` and `site.config.json` instead of hand-editing generated journal HTML.
