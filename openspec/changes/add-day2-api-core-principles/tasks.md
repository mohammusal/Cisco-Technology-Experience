# Tasks

## 1. Scoped Interactive Assets (Present Mode & Offline Widgets)

- [x] 1.1 Create `docs/stylesheets/api-intro.css` scoped strictly to `.api-intro` and `body.api-present-mode` (supporting light & dark Material color schemes, 16:9 Present Mode stage with hidden MkDocs chrome and instructor notes, bottom HUD bar, and clean styling for the Anatomy Explorer, Campus Pizza Playground, Good-vs-Bad Design Flip Cards, and Code Review Quiz); verify zero external URLs or edits to existing stylesheets
- [x] 1.2 Create `docs/assets/javascripts/api-intro.js` implementing Present Mode (`P`, `ArrowRight`, `ArrowLeft`, `Escape` with safe input-focus guard, slide counter, and 30:00 pacing timer), the clickable Request/Response Anatomy Explorer, the offline Campus Pizza API Playground (live in-memory `menu` and `orders` tables, `GET`/`POST`/`PATCH`/`DELETE`, query params `?category=` and `?maxPrice=`, Staff API key `401` guard, `400`/`404` handling, 4 quick-demo presets, and Reset Data), interactive Good-vs-Bad Design Flip Cards, and the 4-question "Code Review This Bad API" challenge with live score; verify valid JS syntax (`node --check` or browser headless check) and zero external resource URLs

## 2. New Day 2 Lab 0 (API Core Principles — 30 min, Zero Webex)

- [x] 2.1 Create `docs/day2/lab0-api-basics.md` (`day: 2`, `lab: 0`) structured into the 9 projector-sized beats around the Campus Pizza / Cafe API domain (The Invisible Bridge, Resources & Endpoints, Request/Response Anatomy Explorer, CRUD Verbs + Status Code Traffic Light, Live Campus Pizza Playground, API Design Part 1 with Flip Cards, API Design Part 2, "Code Review This Bad API" Challenge, and Polling vs Webhooks pizza-buzzer visual + bridge to Lab 1), with collapsed `??? instructor` timing/talking prompts on every beat and `color:#1b242c` on every Mermaid `style` line; verify zero mentions of Webex in the teaching examples and verify `mkdocs build --strict` passes once wired

## 3. Consolidate Old Lab 0 + Lab 1 into Day 2 Lab 1 & Update Navigation

- [x] 3.1 Consolidate `docs/day2/lab0-setup.md` and `docs/day2/lab1-rest.md` into `docs/day2/lab1-rest.md` (`Lab 1 - Setup, Bruno & REST`) organized into Part A (Bruno + Python libraries install, Webex token, `token.txt`, `lab0/setup.py`), Part B (first live Webex call `GET /v1/people/me` + "Break it on purpose" 3 Bruno missions + all 3 annotated Bruno screenshots), and Part C (Bruno -> Python Mermaid bridge + `lab1/get_rooms.py` `TODO 1`–`TODO 4` + Practice + project checkpoint), replacing duplicate theory with a short link back to Lab 0; delete superseded `docs/day2/lab0-setup.md`
- [x] 3.2 Update `mkdocs.yml` (register `stylesheets/api-intro.css` and `assets/javascripts/api-intro.js`, update Day 2 nav to `Lab 0 - API core principles` and `Lab 1 - Setup, Bruno and REST`), `docs/overrides/partials/progress-map.html` (`day2/lab0-api-basics.html` -> `API Basics`, `day2/lab1-rest.html` -> `Setup & REST`), `docs/overrides/home.html` (`Start Day 2` -> `day2/lab0-api-basics.html`), `docs/day2/overview.md`, `docs/day2/lab7-fastapi.md`, and `docs/includes/abbreviations.md` (add `endpoint`, `header`, `stateless`, `status code`); verify `mkdocs build --strict` reports 0 warnings and zero broken links to `lab0-setup`

## 4. End-to-End Verification & Visual Preview (Before Pushing)

- [x] 4.1 Run full automated checks: `python scripts/check_code.py`, `python scripts/package.py` (0 external resource URLs, updated `dist/python-workshop.zip`), and `python scripts/check_diagrams.py` (all Mermaid diagrams parse cleanly and 0 Mermaid fragments leak into `site/search/search_index.json`); verify `git diff` touches zero files under `docs/day1/`, Day 1 `code/`, `code/day2/`, or existing `docs/stylesheets/{extra,callouts,fonts,print}.css`
- [x] 4.2 Capture and visually inspect rendered headless Edge screenshots of `day2/lab0-api-basics.html` in normal mode (light & dark) and Present Mode (including live Playground interaction and Code Review Quiz), plus consolidated `day2/lab1-rest.html`, and verify live local preview on `http://127.0.0.1:8000/Cisco-Technology-Experience/` before pushing

## Workflow follow-up

- After the owner reviews the local preview and approves, commit and push to `origin/main` so GitHub Actions publishes the updated guide to GitHub Pages.
- Archive the completed changes with `/openspec-archive-change`.
