# Design

## Context

See `proposal.md` for motivation and scope. Current technical constraints in this repository:
- Built with MkDocs Material (`use_directory_urls: false`, `mkdocs build --strict`), deployed to GitHub Pages and packaged into an offline student ZIP via `scripts/package.py`.
- `scripts/package.py` fails the build if ANY `.html`, `.css`, or `.js` file in `site/` contains external resource loads (`src="http..."`, `url(http...)`, `@import "http..."`, or `<link href="http...">`).
- `scripts/check_diagrams.py` parses every `<pre class="mermaid">` block using bundled `mermaid.min.js`; every Mermaid `style` line MUST include `color:#1b242c` for dark-mode legibility, and `hooks/search_exclude.py` excludes Mermaid source from `search_index.json`.
- Existing stylesheets (`docs/stylesheets/{fonts,extra,callouts,print}.css`), Day 1 pages/code, and `code/day2/**/*.py` must remain untouched.

## Goals / Non-Goals

**Goals:**
- Deliver a 30-minute, Webex-free, projector-presentable Day 2 Lab 0 (`docs/day2/lab0-api-basics.md`) with zero external runtime dependencies.
- Support both light and dark MkDocs Material color schemes cleanly in normal mode and Present Mode.
- Ensure Present Mode keeps interactive widgets (Anatomy Explorer, Campus Pizza Playground, Design Flip Cards, Code Review Quiz) 100% usable on stage without scrolling overflow on 16:9 screens.
- Keep Day 2's 8-slot progress bar (`Lab 0`–`Lab 7`) and existing `code/day2/` folder structure intact without breaking `scripts/check_code.py`.

**Non-Goals:**
- No backend server, no network calls, and no third-party JS/CSS libraries (pure vanilla ES6 JS + CSS custom properties).
- No changes to Day 1 content/code, Day 2 Labs 2–6 content, or any existing `.py` / `.bru` files in `code/day2/`.
- No Print/PDF export for Present Mode (printing uses standard normal-mode scrolling layout).

## Decisions

### 1. Scoped Assets Instead of Editing Existing Stylesheets
- **Decision**: Create two dedicated local assets — `docs/stylesheets/api-intro.css` and `docs/assets/javascripts/api-intro.js` — registered in `mkdocs.yml` under `extra_css` and `extra_javascript`.
- **Scoping**: Every CSS rule is prefixed with `.api-intro` or `body.api-present-mode`, and `api-intro.js` immediately returns on any page that does not contain `#api-intro-root`.
- **Rationale**: Zero visual or behavioral blast radius on Day 1, Day 2 Labs 1–7, or Help pages; leaves `extra.css`, `callouts.css`, `fonts.css`, and `print.css` completely unmodified.
- **Alternative considered**: Inline `<style>`/`<script>` blocks inside `lab0-api-basics.md` — rejected because large inline JS/CSS hurts Markdown readability, trips MkDocs snippet/highlight edge cases, and is harder to maintain.

### 2. Dual-Mode Architecture (Normal Study View + Present Mode)
- **Structure**: `lab0-api-basics.md` wraps each of its 9 beats in `<section class="api-beat" data-beat="1" data-title="..." data-mins="3" markdown>` inside `<div id="api-intro-root" class="api-intro" markdown>`.
- **Normal Mode (default)**: All 9 beats stack naturally like a normal MkDocs page; a clean banner at the top offers a **Start Present Mode (`P`)** button. Collapsed `??? instructor` admonitions sit inside each beat for self-reference.
- **Present Mode (`body.api-present-mode`)**:
  - Hides `.md-header`, `.md-tabs`, `.md-sidebar`, `.md-footer`, `.md-top`, `.progress-map`, `.api-intro-banner`, and `.admonition.instructor` / `details.instructor`.
  - Shows only `.api-beat.is-active` centered inside a `max-width: 1180px` stage with comfortable projector scaling (`~1.12x–1.2x`, responsive down on smaller laptops so nothing clips).
  - Re-triggers Mermaid sizing if needed when entering Present Mode (Mermaid SVGs render eagerly on initial load because beats are visible by default before Present Mode toggles!).
  - Adds a fixed compact bottom HUD bar: `Prev`, beat dropdown / progress dots (`1 / 9 — Beat Title`), optional **30:00 timer** (Start/Pause/Reset), `Next`, and `Exit (Esc)`.
  - Keyboard shortcuts (`P`, `ArrowRight`, `ArrowLeft`, `Escape`) ignore events when focus is inside `INPUT`, `TEXTAREA`, `SELECT`, or `[contenteditable]`.
- **Alternative considered**: Building a separate Reveal.js slide deck — rejected because Reveal.js adds a heavy third-party dependency, duplicates content between slides and guide, and breaks the unified single-source workshop guide workflow.

### 3. Offline Campus Pizza API Simulator (`api-intro.js`)
- **In-memory state**: Two small seed tables:
  - `menu`: 4 items (`Margherita`, `Pepperoni`, `Veggie`, `Iced Latte`) with `id`, `name`, `category` (`pizza`/`drink`), `price`.
  - `orders`: 2 starter orders (`#101 Ola — Margherita — preparing`, `#102 Jan — Pepperoni — ready`).
- **Supported routes & rules**:
  - `GET /v1/menu` (supports `?category=pizza|drink` and `?maxPrice=N`) -> `200 OK`
  - `GET /v1/menu/:id` -> `200 OK` or `404 Not Found`
  - `DELETE /v1/menu/:id` -> requires `Authorization: Bearer pizza-staff-key` toggle ON (`401 Unauthorized` if OFF; `204 No Content` / `200 OK` if ON; `404` if missing)
  - `GET /v1/orders` & `GET /v1/orders/:id` -> `200 OK` or `404 Not Found`
  - `POST /v1/orders` -> validates JSON + required `item` and `customer` (`400 Bad Request` on invalid JSON or missing fields; `201 Created` on success and appends to `orders`)
  - `PATCH /v1/orders/:id` -> updates `status` (`preparing`/`ready`/`picked_up`) -> `200 OK` or `404`
  - `DELETE /v1/orders/:id` -> requires Staff API key (`401` if OFF; `200 OK` if ON)
  - Any unknown path (e.g. `/v1/burgers`) -> `404 Not Found` with helpful JSON error body
- **Preset quick-demo buttons**: 4 one-click crowd presets (`1. List Menu`, `2. Place Order (201)`, `3. Hack Delete! (401)`, `4. Filter ?category=pizza`) so the instructor can run the live classroom demo smoothly in 60 seconds AND let students type custom edits freely.
- **Offline safety**: Display host prefix as plain text (`api.campuspizza.local`) with relative paths (`/v1/...`) and zero `http://`/`https://` strings matching `package.py`'s resource regexes.

### 4. Interactive Anatomy Explorer & Code Review Quiz
- **Anatomy Explorer (Beat 3)**: Pure HTML buttons representing the 4 Request parts (`POST`, `/v1/orders`, `Authorization + Content-Type`, `{"item":"Margherita","customer":"Ola"}`) and 3 Response parts (`201 Created`, `Content-Type: application/json`, `{"id":103,"status":"preparing"}`). Clicking any token updates a clean explanation card below.
- **Good vs Bad Design Flip Cards (Beat 6)**: Interactive toggle cards comparing messy vs clean REST design (clickable in both normal and Present Mode).
- **Code Review Challenge (Beat 8)**: 4 self-contained multiple-choice cards (1: `POST /deleteOrder?id=5`, 2: `200 OK` with `{"error":"invalid"}`, 3: `GET /v1/orders?api_key=secret123`, 4: `GET /GetPizza` vs `/v1/pizzas`). Clicking an option highlights right/wrong, reveals the design principle, and updates a `Score: X / 4` pill + `Reset Quiz` button.

### 5. Consolidating Old Lab 0 + Lab 1 into Lab 1
- **Decision**: Move the setup + Bruno + token flow from `docs/day2/lab0-setup.md` into `docs/day2/lab1-rest.md` organized into 3 clean parts:
  - **Part A — Setup & Token (`1.1`–`1.3`)**: Install Bruno & Python libraries (`pip install`), get Webex token, save `token.txt`, verify with `lab0/setup.py`.
  - **Part B — Live Webex in Bruno (`1.4`–`1.5`)**: First live call (`GET /v1/people/me` + `bruno-auth-bearer.png` + `bruno-get-me.png`) + "Break it on purpose" 3 missions (`/v1/rooms` -> `200`, `/v1/pizza` -> `404`, damaged token -> `401` + `bruno-error-401.png`, bonus `?max=2`).
  - **Part C — From Bruno to Python (`1.6`–`1.9`)**: Bruno -> Python Mermaid bridge + existing `lab1/get_rooms.py` `TODO 1`–`TODO 4` + Practice + Add it to your project.
- **Remove `docs/day2/lab0-setup.md`** and update all references (`mkdocs.yml`, `progress-map.html`, `home.html`, `day2/overview.md`, `day2/lab7-fastapi.md`) so `mkdocs build --strict` has zero broken links or orphaned pages.
- **Keep `code/day2/lab0/setup.py` in place**: avoids breaking `solutions/lab0_setup.py`, `scripts/check_code.py`, or student handouts, while Lab 1 clearly tells students to open `lab0/setup.py` (Part A) and `lab1/get_rooms.py` (Part C).

## Risks / Trade-offs

- **[Risk] Mermaid diagrams inside `display: none` beats might render with 0 width if hidden before Mermaid initializes** → **Mitigation**: Keep all beats visible by default on page load (normal mode); only hide non-active beats *after* the user activates Present Mode. Every Mermaid SVG is already laid out and rendered cleanly before Present Mode begins.
- **[Risk] Present Mode slide height could overflow on 720p projectors** → **Mitigation**: Keep each beat concise (~1 visual + short bullets or 1 widget), use responsive vertical spacing in `api-intro.css`, and allow smooth inner scrolling only if a screen is very short (`overflow-y: auto` on the stage) so nothing is ever cut off.
- **[Risk] `scripts/package.py` regex false-positives on fake API URLs in JS** → **Mitigation**: Never write `src=`, `url(`, or `@import` with `http(s)://` in `api-intro.js`/`api-intro.css`; use relative paths `/v1/...` and plain text host label `api.campuspizza.local`, and verify 0 external URLs via `scripts/package.py`.
- **[Risk] Deleting `docs/day2/lab0-setup.md` could leave stale links** → **Mitigation**: Grep the entire repo for `lab0-setup` and verify `mkdocs build --strict` passes with zero warnings.
- **[Risk] Dark mode contrast on custom interactive widgets** → **Mitigation**: Style all custom widget surfaces, borders, text, and badges exclusively using existing Material/workshop CSS variables (`--cx-surface`, `--cx-border`, `--cx-ink`, `--cx-muted`, `--cx-blue`, `--cx-green`, `--cx-amber`, `--cx-red`) and verify screenshots in both light and dark modes (plus Present Mode).
