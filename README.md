Personal website hosted on GitHub Pages and mapped to `waynecorrea.com`.

## How This Repo Works

The deployment model is still plain static files in GitHub Pages, but the journal section is now managed through source files and a local build step:

- Edit site-wide metadata in `site.config.json`.
- Edit journal posts in `posts/*.md`.
- Keep `about.html` and `projects.html` as the hand-authored static pages.
- Regenerate the site with `python tools/build_site.py`.

The build script regenerates:

- `index.html`
- `post.html` as a compatibility copy of the latest post
- `posts/*.html` for published journal entries
- `sitemap.xml`
- Post and project dropdown links inside `about.html` and `projects.html`

## Local Workflow

1. Edit the source files locally.
2. Run `python tools/build_site.py`.
3. Preview with `python -m http.server 8000`.
4. Review the generated HTML in a browser.
5. Commit and push the static files to GitHub.

## Notes for Codex

- Treat `posts/*.md` and `site.config.json` as source of truth for journal content.
- Do not hand-edit generated journal pages unless explicitly asked.
- If navigation, post listings, or sitemap entries look stale, rebuild before changing templates by hand.
