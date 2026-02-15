# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Hugo blog (https://yuhi-sa.github.io/) with the `tomatohugo` theme. Japanese default with English translations. Deployed to GitHub Pages via GitHub Actions on push to `main`.

## Commands

```bash
# Dev server
hugo server

# Dev server with drafts
hugo server -D

# Production build (what CI runs)
hugo --gc --minify

# Format check (what CI and pre-commit hook run)
npm run format:check

# Auto-fix formatting
npm run format
```

## Architecture

### Repository Structure

- `config.toml` — Hugo site configuration (languages, menus, params, taxonomies)
- `content/posts/` — Blog posts in Markdown (Japanese `1.md` + English `1.en.md`)
- `themes/tomatohugo/` — Theme as a **git submodule** (`git@github.com:yuhi-sa/tomatohugo.git`); has its own CLAUDE.md with detailed theme architecture
- `public/` — Build output; deployed to `yuhi-sa/yuhi-sa.github.io` repo by CI (not committed here)
- `.github/workflows/deploy.yml` — CI/CD pipeline (Hugo 0.155.3 extended)

### Theme (tomatohugo)

The theme is an independent repository. When modifying theme files, work inside `themes/tomatohugo/` and commit there separately. See `themes/tomatohugo/CLAUDE.md` for theme-specific architecture (template inheritance, partials, asset pipeline, dark mode, SEO).

Key theme paths:

- `layouts/` — Templates (posts/, pages/, taxonomy/, partials/)
- `assets/css/` — Plain CSS with custom properties (variables.css, main.css, syntax.css)
- `assets/js/` — dark-mode.js

### Content Front Matter

Posts support: `title`, `date`, `description`, `tags`, `categories`, `images`, `math` (enables MathJax), `noindex`, `draft`

### Deployment Flow

Push to `main` → GitHub Actions: checkout with submodules → `npm ci` → Prettier check → Hugo build → deploy to `yuhi-sa/yuhi-sa.github.io`

## Conventions

- **Commit messages**: conventional commits — `type(scope): description`
- **Formatting**: Prettier enforced via Lefthook pre-commit hook (CSS/JS/MD checked; HTML templates excluded)
- **CSS**: BEM naming, CSS custom properties for theming, no SCSS
- **Indentation**: 2 spaces
