from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "posts"
CONFIG_PATH = ROOT / "site.config.json"
STATIC_PAGES = [ROOT / "about.html", ROOT / "projects.html"]
SOURCE_EXTENSIONS = {".md", ".html", ".css", ".js", ".json", ".xml", ".txt"}

FRONT_MATTER_BOUNDARY = "---"
POST_LINKS_START = "<!-- Build-time injected links to posts -->"
POST_LINKS_END = "<!-- End of injected links -->"
PROJECT_LINKS_START = "<!-- Build-time injected links to projects -->"
PROJECT_LINKS_END = "<!-- End of injected links -->"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
UL_ITEM_RE = re.compile(r"^(\s*)[-*]\s+(.*)$")
OL_ITEM_RE = re.compile(r"^(\s*)\d+\.\s+(.*)$")
IMAGE_ONLY_RE = re.compile(r"^!\[([^\]]*)\]\(([^)]+)\)$")
INLINE_TOKEN_RE = re.compile(
    r"!\[([^\]]*)\]\(([^)]+)\)|\[(.*?)\]\(([^)]+)\)|\*\*(.+?)\*\*|\*(.+?)\*"
)
MERGE_MARKER_RE = re.compile(r"(?m)^(<<<<<<< .+|=======|>>>>>>> .+)$")


@dataclass
class Post:
    title: str
    author: str
    date: str
    updated: str
    slug: str
    description: str
    excerpt: str
    hero_image: str
    hero_alt: str
    body_markdown: str
    source_path: Path

    @property
    def output_path(self) -> Path:
        return POSTS_DIR / f"{self.slug}.html"

    @property
    def public_url(self) -> str:
        return f"posts/{self.slug}.html"


def main() -> None:
    ensure_clean_sources()
    config = load_config()
    posts = load_posts()
    if not posts:
        raise SystemExit("No published posts found in posts/*.md")

    root_post_dropdown_html = render_post_dropdown_links(posts, in_posts_directory=False)
    posts_post_dropdown_html = render_post_dropdown_links(posts, in_posts_directory=True)
    root_project_dropdown_html = render_project_dropdown_links(
        config["projects_dropdown"],
        prefix="",
    )
    posts_project_dropdown_html = render_project_dropdown_links(
        config["projects_dropdown"],
        prefix="../",
    )

    write_text(ROOT / "index.html", render_index_page(config, posts, root_project_dropdown_html))
    write_text(
        ROOT / "post.html",
        render_post_page(
            config=config,
            post=posts[0],
            post_dropdown_html=root_post_dropdown_html,
            project_dropdown_html=root_project_dropdown_html,
            asset_prefix="posts/",
            stylesheet_href="styles.css",
            script_href="script.js",
            home_href="index.html",
            projects_href="projects.html",
            about_href="about.html",
            canonical_path=f"/{posts[0].public_url}",
        ),
    )

    for post in posts:
        write_text(
            post.output_path,
            render_post_page(
                config=config,
                post=post,
                post_dropdown_html=posts_post_dropdown_html,
                project_dropdown_html=posts_project_dropdown_html,
                asset_prefix="",
                stylesheet_href="../styles.css",
                script_href="../script.js",
                home_href="../index.html",
                projects_href="../projects.html",
                about_href="../about.html",
                canonical_path=f"/{post.public_url}",
            ),
        )

    for page in STATIC_PAGES:
        update_static_page(page, root_post_dropdown_html, root_project_dropdown_html)

    write_text(ROOT / "sitemap.xml", render_sitemap(config, posts))


def ensure_clean_sources() -> None:
    offenders: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.name.endswith(".png") or path.suffix.lower() == ".pdf":
            continue
        if path.suffix.lower() not in SOURCE_EXTENSIONS:
            continue
        text = path.read_text(encoding="utf-8")
        if MERGE_MARKER_RE.search(text):
            offenders.append(str(path.relative_to(ROOT)))
    if offenders:
        joined = ", ".join(sorted(offenders))
        raise SystemExit(f"Resolve merge markers before building: {joined}")


def load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def load_posts() -> list[Post]:
    posts: list[Post] = []
    for path in sorted(POSTS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8").strip()
        if not text:
            continue
        front_matter, body = parse_front_matter(text, path)
        if front_matter.get("draft", False):
            continue

        title = require_string(front_matter, "title", path)
        author = str(front_matter.get("author", front_matter.get("Author", "Wayne Correa")))
        date = require_string(front_matter, "date", path)
        updated = str(front_matter.get("updated", date))
        slug = str(front_matter.get("slug", slugify(title)))
        description = str(front_matter.get("description", "")).strip()
        excerpt = str(front_matter.get("excerpt", "")).strip()
        hero_image = str(front_matter.get("hero_image", "")).strip()
        hero_alt = str(front_matter.get("hero_alt", "")).strip()

        if not description:
            description = excerpt or first_paragraph(body)
        if not excerpt:
            excerpt = first_paragraph(body)

        posts.append(
            Post(
                title=title,
                author=author,
                date=date,
                updated=updated,
                slug=slug,
                description=description,
                excerpt=excerpt,
                hero_image=hero_image,
                hero_alt=hero_alt,
                body_markdown=body.strip(),
                source_path=path,
            )
        )

    return sorted(posts, key=lambda post: (post.date, post.slug), reverse=True)


def parse_front_matter(text: str, path: Path) -> tuple[dict, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != FRONT_MATTER_BOUNDARY:
        raise SystemExit(f"{path.relative_to(ROOT)} must start with YAML front matter")

    try:
        boundary_index = lines[1:].index(FRONT_MATTER_BOUNDARY) + 1
    except ValueError as error:
        raise SystemExit(f"{path.relative_to(ROOT)} is missing a closing front matter boundary") from error

    front_matter_lines = lines[1:boundary_index]
    body = "\n".join(lines[boundary_index + 1 :]).strip()
    return parse_front_matter_lines(front_matter_lines), body


def parse_front_matter_lines(lines: list[str]) -> dict:
    data: dict[str, object] = {}
    current_list_key: str | None = None

    for raw_line in lines:
        if not raw_line.strip():
            continue
        if raw_line.startswith("  - "):
            if current_list_key is None:
                raise SystemExit("List item found before a list key in front matter")
            data.setdefault(current_list_key, [])
            assert isinstance(data[current_list_key], list)
            data[current_list_key].append(raw_line[4:].strip())
            continue

        current_list_key = None
        if ":" not in raw_line:
            raise SystemExit(f"Invalid front matter line: {raw_line}")
        key, raw_value = raw_line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()
        if not value:
            data[key] = []
            current_list_key = key
            continue
        lowered = value.lower()
        if lowered == "true":
            data[key] = True
        elif lowered == "false":
            data[key] = False
        else:
            data[key] = value

    return data


def require_string(front_matter: dict, key: str, path: Path) -> str:
    value = str(front_matter.get(key, "")).strip()
    if not value:
        raise SystemExit(f"{path.relative_to(ROOT)} is missing required front matter: {key}")
    return value


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "post"


def first_paragraph(markdown: str) -> str:
    for block in markdown.split("\n\n"):
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if not lines:
            continue
        if lines[0].startswith("#"):
            continue
        if UL_ITEM_RE.match(lines[0]) or OL_ITEM_RE.match(lines[0]):
            continue
        cleaned = " ".join(lines)
        return strip_markdown(cleaned)
    return ""


def strip_markdown(text: str) -> str:
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r"\1", text)
    text = re.sub(r"\[(.*?)\]\(([^)]+)\)", r"\1", text)
    text = text.replace("**", "").replace("*", "")
    return " ".join(text.split())


def render_inline(text: str, *, image_prefix: str = "") -> str:
    parts: list[str] = []
    position = 0
    for match in INLINE_TOKEN_RE.finditer(text):
        parts.append(html.escape(text[position : match.start()]))
        image_alt, image_src, link_text, link_href, strong_text, em_text = match.groups()
        if image_src is not None:
            parts.append(
                f'<img src="{html.escape(prefix_asset_path(image_src, image_prefix), quote=True)}" alt="{html.escape(image_alt, quote=True)}" loading="lazy">'
            )
        elif link_href is not None:
            parts.append(
                f'<a href="{html.escape(link_href, quote=True)}">{html.escape(link_text)}</a>'
            )
        elif strong_text is not None:
            parts.append(f"<strong>{html.escape(strong_text)}</strong>")
        elif em_text is not None:
            parts.append(f"<em>{html.escape(em_text)}</em>")
        position = match.end()
    parts.append(html.escape(text[position:]))
    return "".join(parts)


def render_markdown(markdown: str, *, image_prefix: str = "") -> str:
    lines = markdown.splitlines()
    blocks, _ = parse_blocks(lines, 0, image_prefix=image_prefix)
    return "\n".join(blocks)


def parse_blocks(lines: list[str], start_index: int, *, image_prefix: str) -> tuple[list[str], int]:
    blocks: list[str] = []
    index = start_index

    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue

        if HEADING_RE.match(line.strip()):
            match = HEADING_RE.match(line.strip())
            assert match is not None
            level = len(match.group(1))
            blocks.append(f"<h{level}>{render_inline(match.group(2).strip(), image_prefix=image_prefix)}</h{level}>")
            index += 1
            continue

        if UL_ITEM_RE.match(line) or OL_ITEM_RE.match(line):
            list_html, index = parse_list(lines, index, image_prefix=image_prefix)
            blocks.append(list_html)
            continue

        image_match = IMAGE_ONLY_RE.match(line.strip())
        if image_match:
            blocks.append(
                f'<p><img src="{html.escape(prefix_asset_path(image_match.group(2), image_prefix), quote=True)}" alt="{html.escape(image_match.group(1), quote=True)}" loading="lazy"></p>'
            )
            index += 1
            continue

        paragraph_lines = [line.strip()]
        index += 1
        while index < len(lines):
            next_line = lines[index]
            if not next_line.strip():
                break
            if HEADING_RE.match(next_line.strip()) or UL_ITEM_RE.match(next_line) or OL_ITEM_RE.match(next_line):
                break
            paragraph_lines.append(next_line.strip())
            index += 1
        blocks.append(f"<p>{render_inline(' '.join(paragraph_lines), image_prefix=image_prefix)}</p>")

    return blocks, index


def parse_list(lines: list[str], start_index: int, *, image_prefix: str) -> tuple[str, int]:
    first_line = lines[start_index]
    is_ordered = OL_ITEM_RE.match(first_line) is not None
    matcher = OL_ITEM_RE if is_ordered else UL_ITEM_RE
    first_match = matcher.match(first_line)
    assert first_match is not None
    list_indent = len(first_match.group(1).replace("\t", "    "))
    tag = "ol" if is_ordered else "ul"

    items: list[str] = []
    index = start_index
    while index < len(lines):
        line = lines[index]
        match = matcher.match(line)
        if match is None:
            break
        indent = len(match.group(1).replace("\t", "    "))
        if indent != list_indent:
            break

        item_lead = match.group(2).strip()
        index += 1
        item_lines: list[str] = []

        while index < len(lines):
            next_line = lines[index]
            if not next_line.strip():
                item_lines.append("")
                index += 1
                continue

            next_indent = leading_spaces(next_line)
            next_ul = UL_ITEM_RE.match(next_line)
            next_ol = OL_ITEM_RE.match(next_line)
            if next_ul or next_ol:
                if next_indent < list_indent:
                    break
                if next_indent == list_indent:
                    break
            elif next_indent <= list_indent:
                break

            item_lines.append(next_line)
            index += 1

        items.append(render_list_item(item_lead, item_lines, image_prefix=image_prefix))

    return f"<{tag}>\n" + "\n".join(items) + f"\n</{tag}>", index


def render_list_item(item_lead: str, item_lines: list[str], *, image_prefix: str) -> str:
    meaningful_lines = [line for line in item_lines if line.strip()]
    if not meaningful_lines:
        return f"<li>{render_inline(item_lead, image_prefix=image_prefix)}</li>"

    dedented_lines = dedent_lines(item_lines)
    child_blocks, _ = parse_blocks(dedented_lines, 0, image_prefix=image_prefix)
    child_html = "\n".join(child_blocks)
    lead_html = f"<p>{render_inline(item_lead, image_prefix=image_prefix)}</p>" if item_lead else ""
    return f"<li>{lead_html}{child_html}</li>"


def dedent_lines(lines: list[str]) -> list[str]:
    non_blank_indents = [
        len(line) - len(line.lstrip(" "))
        for line in lines
        if line.strip()
    ]
    if not non_blank_indents:
        return lines
    trim = min(non_blank_indents)
    return [line[trim:] if len(line) >= trim else line for line in lines]


def render_post_dropdown_links(posts: list[Post], *, in_posts_directory: bool) -> str:
    return "\n".join(
        (
            f'                                <li><a href="{post.slug}.html">{html.escape(post.title)}</a></li>'
            if in_posts_directory
            else f'                                <li><a href="{post.public_url}">{html.escape(post.title)}</a></li>'
        )
        for post in posts
    )


def render_project_dropdown_links(projects: list[dict], *, prefix: str) -> str:
    return "\n".join(
        f'                                <li><a href="{html.escape(prefix + project["href"], quote=True)}">{html.escape(project["label"])}</a></li>'
        for project in projects
    )


def render_head(
    *,
    config: dict,
    title: str,
    description: str,
    canonical_path: str,
    og_type: str,
    extra_meta: str,
    structured_data: str,
    stylesheet_href: str,
) -> str:
    site_url = config["site_url"].rstrip("/")
    canonical_url = f"{site_url}{canonical_path}"
    social_image_url = f'{site_url}/{config["social_image"].lstrip("/")}'
    analytics_id = config["analytics_website_id"]
    page_title = f"{title} | {config['site_name']}" if title != config["site_name"] else config["site_name"]

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{html.escape(description, quote=True)}">
    <meta name="author" content="{html.escape(config["site_name"], quote=True)}">
    <meta name="robots" content="index, follow">
    <meta name="color-scheme" content="dark light">
    <meta name="theme-color" content="{html.escape(config["theme_color"], quote=True)}">
    <link rel="canonical" href="{html.escape(canonical_url, quote=True)}">
    <meta property="og:title" content="{html.escape(page_title, quote=True)}">
    <meta property="og:description" content="{html.escape(description, quote=True)}">
    <meta property="og:type" content="{html.escape(og_type, quote=True)}">
    <meta property="og:url" content="{html.escape(canonical_url, quote=True)}">
    <meta property="og:site_name" content="{html.escape(config["site_name"], quote=True)}">
    <meta property="og:image" content="{html.escape(social_image_url, quote=True)}">
    <meta property="og:image:alt" content="{html.escape(config["site_name"], quote=True)} portfolio preview">
    <meta property="og:locale" content="en_US">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{html.escape(page_title, quote=True)}">
    <meta name="twitter:description" content="{html.escape(description, quote=True)}">
    <meta name="twitter:image" content="{html.escape(social_image_url, quote=True)}">
    {extra_meta}
    <title>{html.escape(page_title)}</title>
    <link rel="stylesheet" href="{html.escape(stylesheet_href, quote=True)}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/feather-icons/dist/feather.min.js"></script>
    <script type="application/ld+json">
{structured_data}
    </script>
    <script defer src="https://cloud.umami.is/script.js" data-website-id="{html.escape(analytics_id, quote=True)}"></script>
</head>"""


def render_header(
    *,
    active_section: str,
    config: dict,
    post_dropdown_html: str,
    project_dropdown_html: str,
    home_href: str,
    projects_href: str,
    about_href: str,
) -> str:
    journal_active = " active" if active_section == "journal" else ""
    projects_active = " active" if active_section == "projects" else ""
    about_active = " active" if active_section == "about" else ""
    return f"""    <header class="site-header">
        <div class="container">
            <div class="header-content">
                <div class="header-identity">
                    <h1 class="header-name">{html.escape(config["site_name"])}</h1>
                    <div class="header-contact-links">
                        <a href="mailto:{html.escape(config["email"], quote=True)}"><i data-feather="mail"></i> {html.escape(config["email"])}</a>
                        <a href="{html.escape(config["linkedin_url"], quote=True)}" target="_blank" rel="noopener noreferrer"><i data-feather="linkedin"></i> LinkedIn</a>
                    </div>
                </div>
                <nav class="main-nav">
                    <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
                        <i data-feather="menu"></i>
                    </button>
                    <ul class="nav-menu">
                        <li class="dropdown">
                            <a href="{html.escape(home_href, quote=True)}" class="nav-link{journal_active}" aria-haspopup="true">My Journal <i data-feather="chevron-down"></i></a>
                            <ul class="dropdown-menu">
{POST_LINKS_START}
{post_dropdown_html}
{POST_LINKS_END}
                            </ul>
                        </li>
                        <li class="dropdown">
                            <a href="{html.escape(projects_href, quote=True)}" class="nav-link{projects_active}" aria-haspopup="true">Projects <i data-feather="chevron-down"></i></a>
                            <ul class="dropdown-menu">
{PROJECT_LINKS_START}
{project_dropdown_html}
{PROJECT_LINKS_END}
                            </ul>
                        </li>
                        <li class="dropdown">
                            <a href="{html.escape(about_href, quote=True)}" class="nav-link{about_active}" aria-haspopup="true">About Me <i data-feather="chevron-down"></i></a>
                            <ul class="dropdown-menu">
                                <li><a href="{html.escape(about_href, quote=True)}#about">About</a></li>
                                <li><a href="{html.escape(about_href, quote=True)}#progression">Career</a></li>
                                <li><a href="{html.escape(about_href, quote=True)}#achievements">Impact</a></li>
                                <li><a href="{html.escape(about_href, quote=True)}#expertise">Expertise</a></li>
                                <li><a href="{html.escape(about_href, quote=True)}#experience">Experience</a></li>
                                <li><a href="{html.escape(about_href, quote=True)}#contact">Contact</a></li>
                            </ul>
                        </li>
                    </ul>
                    <div class="settings-dropdown">
                        <button class="settings-toggle" aria-label="Settings">
                            <i data-feather="settings"></i>
                        </button>
                        <div class="settings-menu">
                            <div class="settings-section">
                                <label for="theme-select">Theme</label>
                                <select id="theme-select">
                                    <option value="light">Light</option>
                                    <option value="dark">Dark</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </nav>
            </div>
        </div>
    </header>"""


def render_footer(config: dict) -> str:
    return f"""    <footer class="site-footer-main">
        <div class="container">
            <div class="footer-content">
                <div class="footer-contact">
                    <h3>{html.escape(config["site_name"])}</h3>
                    <a href="mailto:{html.escape(config["email"], quote=True)}">{html.escape(config["email"])}</a>
                </div>
                <div class="footer-links">
                    <a href="{html.escape(config["linkedin_url"], quote=True)}" target="_blank" rel="noopener noreferrer">LinkedIn</a>
                </div>
            </div>
            <div class="footer-copyright">
                <p>&copy; 2026 {html.escape(config["site_name"])}. All rights reserved.</p>
            </div>
        </div>
    </footer>"""


def render_index_page(config: dict, posts: list[Post], project_dropdown_html: str) -> str:
    description = (
        "Journal and insights from Wayne Correa, a cloud infrastructure product leader "
        "focused on cloud networking, product strategy, and leadership."
    )
    structured_data = json.dumps(
        {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "Person",
                    "@id": f'{config["site_url"]}/#waynecorrea',
                    "name": config["site_name"],
                    "url": config["site_url"],
                    "jobTitle": "Cloud Infrastructure Product Leader",
                    "sameAs": [config["linkedin_url"]],
                },
                {
                    "@type": "WebSite",
                    "name": config["site_name"],
                    "url": config["site_url"],
                    "publisher": {"@id": f'{config["site_url"]}/#waynecorrea'},
                },
            ],
        },
        indent=8,
    )

    journal_cards = []
    for index, post in enumerate(posts):
        separator = '\n            <hr class="post-separator">\n' if index < len(posts) - 1 else ""
        journal_cards.append(
            f"""            <article class="journal-post">
                <header class="post-header">
                    <h3 class="post-title"><a href="{post.public_url}">{html.escape(post.title)}</a></h3>
                    <p class="post-meta">Published on <time datetime="{html.escape(post.date, quote=True)}">{human_date(post.date)}</time></p>
                </header>
                <div class="post-excerpt">
                    <p>{html.escape(post.excerpt)}</p>
                </div>
                <a href="{post.public_url}" class="btn btn-secondary">Read More</a>
            </article>{separator}"""
        )

    return f"""{render_head(
    config=config,
    title="My Journal",
    description=description,
    canonical_path="/",
    og_type="website",
    extra_meta="",
    structured_data=structured_data,
    stylesheet_href="styles.css",
)}
<body data-theme="dark">
<!-- Generated by tools/build_site.py; edit posts/*.md or site.config.json instead of this file. -->
{render_header(
    active_section="journal",
    config=config,
    post_dropdown_html=render_post_dropdown_links(posts, in_posts_directory=False),
    project_dropdown_html=project_dropdown_html,
    home_href="index.html",
    projects_href="projects.html",
    about_href="about.html",
)}

    <main class="container page-main">
        <h2 class="section-title">My Journal</h2>
        <div class="journal-list">
{''.join(journal_cards)}
        </div>
    </main>

{render_footer(config)}

    <script src="script.js"></script>
</body>
</html>
"""


def render_post_page(
    *,
    config: dict,
    post: Post,
    post_dropdown_html: str,
    project_dropdown_html: str,
    asset_prefix: str,
    stylesheet_href: str,
    script_href: str,
    home_href: str,
    projects_href: str,
    about_href: str,
    canonical_path: str,
) -> str:
    description = post.description
    structured_data = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": post.title,
            "datePublished": post.date,
            "dateModified": post.updated,
            "author": {
                "@type": "Person",
                "name": post.author,
                "url": config["site_url"],
            },
            "publisher": {
                "@type": "Person",
                "name": config["site_name"],
                "url": config["site_url"],
            },
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": f'{config["site_url"]}{canonical_path}',
            },
            "image": [f'{config["site_url"]}/{config["social_image"]}'],
            "description": description,
        },
        indent=8,
    )
    hero_image_html = ""
    if post.hero_image:
        hero_image_html = (
            f'\n                <img src="{html.escape(prefix_asset_path(post.hero_image, asset_prefix), quote=True)}" '
            f'alt="{html.escape(post.hero_alt, quote=True)}" loading="lazy">'
        )

    return f"""{render_head(
    config=config,
    title=post.title,
    description=description,
    canonical_path=canonical_path,
    og_type="article",
    extra_meta=(
        f'<meta property="article:published_time" content="{html.escape(post.date, quote=True)}">\n'
        f'    <meta property="article:modified_time" content="{html.escape(post.updated, quote=True)}">'
    ),
    structured_data=structured_data,
    stylesheet_href=stylesheet_href,
)}
<body data-theme="dark">
<!-- Generated by tools/build_site.py; edit posts/*.md or site.config.json instead of this file. -->
{render_header(
    active_section="journal",
    config=config,
    post_dropdown_html=post_dropdown_html,
    project_dropdown_html=project_dropdown_html,
    home_href=home_href,
    projects_href=projects_href,
    about_href=about_href,
)}

    <main class="container page-main">
        <article class="post-full">
            <header class="post-full-header">
                <h1 class="post-full-title">{html.escape(post.title)}</h1>
                <p class="post-meta">Published on <time datetime="{html.escape(post.date, quote=True)}">{human_date(post.date)}</time> by {html.escape(post.author)}</p>{hero_image_html}
            </header>

            <div class="post-full-content">
{indent(render_markdown(post.body_markdown, image_prefix=asset_prefix), 16)}
            </div>
        </article>
    </main>

{render_footer(config)}

    <script src="{html.escape(script_href, quote=True)}"></script>
</body>
</html>
"""


def indent(text: str, spaces: int) -> str:
    prefix = " " * spaces
    return "\n".join(f"{prefix}{line}" if line else "" for line in text.splitlines())


def human_date(value: str) -> str:
    year, month, day = value.split("-")
    months = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    }
    return f"{months[month]} {int(day)}, {year}"


def leading_spaces(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def prefix_asset_path(path: str, prefix: str) -> str:
    if not prefix:
        return path
    if "://" in path or path.startswith("/") or path.startswith("#"):
        return path
    return f"{prefix}{path}"


def update_static_page(path: Path, post_dropdown_html: str, project_dropdown_html: str) -> None:
    text = path.read_text(encoding="utf-8")
    text = replace_marker_block(text, POST_LINKS_START, POST_LINKS_END, post_dropdown_html)
    text = replace_marker_block(text, PROJECT_LINKS_START, PROJECT_LINKS_END, project_dropdown_html)
    text = text.replace("http://cloudinfrastructure.org", "https://cloudinfrastructure.org")
    write_text(path, text)


def replace_marker_block(text: str, start_marker: str, end_marker: str, replacement: str) -> str:
    pattern = re.compile(
        rf"({re.escape(start_marker)}\n)(.*?)(\n\s*{re.escape(end_marker)})",
        re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"Could not find marker block: {start_marker}")
    return text[: match.start()] + match.group(1) + replacement + match.group(3) + text[match.end() :]


def render_sitemap(config: dict, posts: list[Post]) -> str:
    base_url = config["site_url"].rstrip("/")
    urls = [
        ("", posts[0].updated, "1.0"),
        ("about.html", posts[0].updated, "0.8"),
        ("projects.html", posts[0].updated, "0.8"),
    ]
    urls.extend((post.public_url, post.updated, "0.6") for post in posts)

    entries = []
    for path, lastmod, priority in urls:
        location = base_url if not path else f"{base_url}/{path}"
        entries.append(
            "    <url>\n"
            f"        <loc>{html.escape(location)}</loc>\n"
            f"        <lastmod>{html.escape(lastmod)}</lastmod>\n"
            f"        <priority>{html.escape(priority)}</priority>\n"
            "    </url>"
        )

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(entries)
        + "\n</urlset>\n"
    )


def write_text(path: Path, content: str) -> None:
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
