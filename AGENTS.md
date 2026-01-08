# Repository Guidelines

## Project Structure & Module Organization
- `index.html`, `about.html`, `projects.html`, `post.html`: Page templates and content markup.
- `styles.css`: Global styles, CSS variables, and responsive rules.
- `script.js`: Vanilla JS behavior (navigation, theme, UI interactions).
- `posts/`: Markdown source for journal posts (for example, `posts/week2.md`).
- `screen.png`: Static asset used in the site.
- `CNAME`: Custom domain for GitHub Pages.

## Build, Test, and Development Commands
- No build step or dependencies. Edit files directly.
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
  - Desktop and mobile widths (320px, 768px, 1440px).
  - Navigation, dropdowns, and theme toggle.
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
