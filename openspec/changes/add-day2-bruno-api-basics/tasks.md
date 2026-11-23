# Tasks

## 1. Bruno Starter Collection and Annotated Screenshots

- [x] 1.1 Create the 5-file plain-text Bruno starter collection under `code/day2/bruno-collection/` (`bruno.json`, `environments/Webex.bru` with `PASTE_YOUR_TOKEN_HERE` only, `Who am I.bru`, `List rooms.bru`, `Break it 404.bru`); verify `bruno.json` parses as valid JSON, every `.bru` file uses `{{token}}` with zero real tokens, and `scripts/check_code.py` still passes
- [x] 1.2 Create the 3 annotated Bruno PNG screenshots under `docs/assets/screens/` (`bruno-auth-bearer.png`, `bruno-get-me.png`, `bruno-error-401.png`) matching Day 1's crisp ~1560px annotated style with numbered red callouts and sample student `Ola Nowak` (zero real tokens or personal data); verify each image visually via Read

## 2. Upgrade Day 2 Lab 0 and Lab 1 (Short, Visual, Interactive)

- [x] 2.1 Update `docs/day2/lab0-setup.md` with the short API basics hook (everyday apps Mermaid diagram, 4-verb `GET/POST/PUT/DELETE` table, interactive "API Detective" `predict` puzzle), compact Bruno install step (Windows/Mac tabs), and "Your first API call in Bruno" (`GET https://webexapis.com/v1/people/me` + `bruno-auth-bearer.png` + `bruno-get-me.png` + 1-click collection fallback) while keeping existing `pip install`, `token.txt`, and `lab0/setup.py` steps intact; verify `mkdocs build --strict` passes
- [x] 2.2 Update `docs/day2/lab1-rest.md` with the Status Code traffic-light Mermaid diagram (`2xx`/`4xx`/`5xx`), "Break It on Purpose" Bruno missions (`/v1/rooms` -> `200`, `/v1/pizza` -> `404`, broken token -> `401`, bonus `?max=2`) with `bruno-error-401.png`, and the **Bruno -> Python** Mermaid bridge diagram leading into the unchanged `TODO 1`–`TODO 4` Python steps; verify `mkdocs build --strict` passes

## 3. Supporting Day 2 Pages and Glossary

- [x] 3.1 Update `docs/day2/overview.md` (mention Bruno in Lab 0 and Lab 1 rows), `docs/day2/cheat-sheet.md` (add a compact 4-verb HTTP methods box while keeping the cheat sheet compact), and `docs/includes/abbreviations.md` (add `Bruno` and `HTTP`); verify `mkdocs build --strict` passes and the terms appear in `site/help/glossary.html`

## 4. Local Verification and Visual Review (Before Pushing)

- [x] 4.1 Run full local checks: `python scripts/check_code.py`, `python scripts/package.py` (0 external URLs, `bruno-collection/` and new screenshots packaged in `dist/python-workshop.zip`), `python scripts/check_diagrams.py` (all Mermaid diagrams parse cleanly and carry `data-search-exclude`), and confirm `git diff` touches zero files under `docs/day1/`, `docs/stylesheets/`, Day 1 `code/`, or existing `code/day2/**/*.py`
- [x] 4.2 Capture and inspect rendered screenshots of the updated `day2/lab0-setup.html` and `day2/lab1-rest.html` (and verify live reload on `http://127.0.0.1:8000/Cisco-Technology-Experience/`) so the owner can review locally before committing or pushing

## Workflow follow-up

- After the owner approves the local preview, commit and push both Day 2 changes to `origin/main` so GitHub Actions publishes the updated guide to GitHub Pages.
- Archive the completed changes with `/openspec-archive-change`.
