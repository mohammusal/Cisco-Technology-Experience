# Tasks

## 1. Day 2 Student Code and Token Protection

- [x] 1.1 Copy all 25 Day 2 files from `C:\Users\mohamusa\Downloads\python-workshop\code\day2` into `code/day2/` without modifying any Day 1 files under `code/`; verify `code/day2/` contains all 25 files and `git diff code/` shows zero changes to Day 1 files
- [x] 1.2 Add `code/**/token.txt` and `token.txt` to `.gitignore`, and add `"token.txt"` to `SKIP_IN_CODE` in `scripts/package.py`; verify a temporary `code/day2/token.txt` is ignored by `git status` and excluded from `dist/python-workshop/code/day2/` while `token.example.txt` remains included
- [x] 1.3 Extend `scripts/check_code.py` with offline Day 2 checks (syntax-check all `code/day2/**/*.py`, verify `# TODO ` markers in starters, run `lab0/setup.py`, `lab1/get_rooms.py`, `solutions/lab1_get_rooms.py`, `solutions/lab1_exercise.py`, and `solutions/lab0_setup.py` with and without a temp `token.txt`) without changing any Day 1 checks; verify `python scripts/check_code.py` passes cleanly

## 2. Day 2 Guide Pages (Reconstructed from Colleague Handout)

- [x] 2.1 Reconstruct `docs/day2/overview.md`, `docs/day2/cheat-sheet.md`, and `docs/day2/lab0-setup.md` through `docs/day2/lab3-members.md` from `C:\Users\mohamusa\Downloads\python-workshop\guide\day2\*.html` using this guide's front matter (`day: 2`, `lab: 0..3`), layout classes, admonitions, tabs, and Mermaid diagrams; verify each page's headings, code blocks, and Mermaid count match the source HTML
- [x] 2.2 Reconstruct `docs/day2/lab4-messages.md` through `docs/day2/lab7-fastapi.md` from `C:\Users\mohamusa\Downloads\python-workshop\guide\day2\*.html` with front matter (`day: 2`, `lab: 4..7`), admonitions, tabs, and Mermaid diagrams; verify each page's headings, code blocks, and Mermaid count match the source HTML

## 3. Shared Navigation, Home Page, Progress Bar, and Help Pages

- [x] 3.1 Update `docs/overrides/partials/progress-map.html` to branch on `page.meta.day | default(1)` for Day 2 labs while leaving Day 1's stepper identical; verify Day 1 lab pages still show the 8 Day 1 steps and Day 2 lab pages show the 8 Day 2 steps
- [x] 3.2 Update `docs/overrides/home.html` with Day 2 entry points (`Start Day 1` / `Start Day 2` buttons and the `Day 2 - Webex APIs` card) using our existing home CSS unchanged, and add the `Webex APIs` tab (`day2/*`) to `mkdocs.yml` without modifying `Python Basics` or `docs/stylesheets/*`; verify `mkdocs build --strict` exits 0 with zero warnings
- [x] 3.3 Append the 3 Day 2 troubleshooting entries (`Webex returns 401 Unauthorized`, `Webex returns 409 Conflict`, `Flask or uvicorn cannot start`) to `docs/help/troubleshooting.md` and the 9 Day 2 glossary terms (`API`, `bot`, `FastAPI`, `Flask`, `JSON`, `REST`, `SDK`, `token`, `webhook`) to `docs/includes/abbreviations.md`; verify all new entries appear in `site/help/troubleshooting.html` and `site/help/glossary.html`

## 4. Integration Checks and Local Preview (Before Pushing)

- [x] 4.1 Run full local verification: `python scripts/check_code.py`, `python scripts/package.py` (0 external resource URLs), `python scripts/check_diagrams.py` (all 77 diagrams = 63 Day 1 + 14 Day 2 parse cleanly and carry `data-search-exclude`), and confirm `git diff` touches zero files under `docs/day1/`, `docs/stylesheets/`, or Day 1 `code/`
- [x] 4.2 Start a local preview (`mkdocs serve`) and inspect Home, Day 1 (unchanged), Day 2 overview, Day 2 labs (stepper + Mermaid diagrams), Cheat Sheet, and Help pages so the owner can review the combined site locally before any commit or push

## Workflow follow-up

- After the owner reviews and approves the local preview, commit and push to `origin/main` so GitHub Actions publishes the combined Day 1 + Day 2 guide to GitHub Pages.
- Archive the change with `/openspec-archive-change` once live verification is complete.
