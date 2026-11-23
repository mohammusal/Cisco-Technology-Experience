# Proposal

## Why

A colleague created the Day 2 (Webex APIs) workshop track—10 guide pages with 14 Mermaid diagrams and 25 starter/solution Python files—and delivered it as a packaged handout in `C:\Users\mohamusa\Downloads\python-workshop`. Merging Day 2 into this MkDocs repository brings both days together under one site and offline handout while keeping Day 1 and the site's visual styling untouched, and lets the owner verify the combined site locally before anything is pushed to GitHub.

## What Changes

- **Add Day 2 starter and solution code** under `code/day2/` (25 files: `config.py`, `webex_project.py`, `rooms_sample.json`, `token.example.txt`, `lab0/`–`lab7/`, and `solutions/`).
- **Add Day 2 MkDocs guide pages** under `docs/day2/` (10 pages: `overview.md`, `lab0-setup.md` through `lab7-fastapi.md`, and `cheat-sheet.md`) reconstructed from `C:\Users\mohamusa\Downloads\python-workshop\guide\day2\*.html` using this guide's existing styling, components, and Mermaid diagram conventions.
- **Wire Day 2 into shared navigation and entry points**:
  - Add a **Webex APIs** navigation tab to `mkdocs.yml` alongside **Python Basics**.
  - Update `docs/overrides/home.html` with Day 2 entry points (**Start Day 2** button and **Day 2 – Webex APIs** card) while preserving the existing visual styling.
  - Extend `docs/overrides/partials/progress-map.html` to render the Day 2 lab stepper when page front matter sets `day: 2`, leaving Day 1's stepper unchanged.
- **Extend shared Help pages** with Day 2 items:
  - Append 3 Day 2 troubleshooting entries (`Webex returns 401 Unauthorized`, `Webex returns 409 Conflict`, `Flask or uvicorn cannot start`) to `docs/help/troubleshooting.md`.
  - Add 9 Day 2 glossary terms (`API`, `bot`, `FastAPI`, `Flask`, `JSON`, `REST`, `SDK`, `token`, `webhook`) to `docs/includes/abbreviations.md`.
- **Protect Webex tokens from leaking**: ignore `token.txt` in `.gitignore` and in `SKIP_IN_CODE` inside `scripts/package.py`.
- **Extend automated offline code checks**: add Day 2 offline checks (run `lab0` and `lab1` offline against `rooms_sample.json`, and syntax-check `lab2`–`lab7` and solutions without calling Webex) to `scripts/check_code.py`, leaving all Day 1 checks unchanged.
- **Leave Day 1 and site styling untouched**: no edits to `docs/day1/*`, Day 1 code/solutions (`code/lab0`–`code/lab7`, `code/quiz.py`, `code/questions.py`, `code/solutions/*`), or `docs/stylesheets/*`.
- **Local preview before publishing**: stop after local build, automated checks, and `mkdocs serve` verification; do not commit or push to GitHub until the owner reviews the local site.

## Capabilities

### New Capabilities
- `day2-webex-guide`: Day 2 Webex APIs lab guide pages, student starter/solution code, dual-day navigation/progress stepper, token leak prevention, and offline code verification.

### Modified Capabilities
<!-- None: openspec/specs/ currently has no synced specs; existing Day 1 behavior and styling remain unchanged. -->

## Impact

- **Docs & Templates**: `docs/day2/*.md` (new), `docs/overrides/home.html`, `docs/overrides/partials/progress-map.html`, `docs/help/troubleshooting.md`, `docs/includes/abbreviations.md`, `mkdocs.yml`.
- **Student Code**: `code/day2/**` (new, 25 files).
- **Tooling & Hygiene**: `.gitignore`, `scripts/package.py`, `scripts/check_code.py`.
- **Build & CI**: Existing `mkdocs build --strict`, `scripts/package.py`, `scripts/check_diagrams.py`, and `.github/workflows/pages.yml` automatically validate and publish Day 2 once pushed; no new CI runtime dependencies are required because Day 2 checks run offline using Python's standard library.
- **Untouched**: `docs/day1/*`, `docs/stylesheets/*`, `code/lab0`–`code/lab7`, `code/quiz.py`, `code/questions.py`, `code/solutions/*`, and the live GitHub Pages site until the owner chooses to push.
