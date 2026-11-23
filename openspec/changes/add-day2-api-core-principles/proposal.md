# Proposal

## Why

Day 2 currently jumps straight from the roadmap into Webex token setup and Bruno, leaving instructors without a dedicated, vendor-neutral 30-minute foundation to teach high-school graduates what APIs are, how HTTP requests/responses work, and how good APIs are designed. Because the instructor presents directly from this workshop guide with no separate slide deck, the guide needs a projector-ready, visual, and interactive Lab 0 covering pure API core principles before students touch Webex in Lab 1.

## What Changes

- **New Day 2 Lab 0 — API Core Principles (`docs/day2/lab0-api-basics.md`)**: Add a 30-minute, Webex-free, interactive theory & design module built around a single relatable domain (**Campus Pizza / Cafe API**: `/v1/menu`, `/v1/orders`) in 9 projector-sized beats:
  1. The Invisible Bridge (why APIs exist, why apps never talk straight to databases)
  2. Resources & Endpoints (nouns, hierarchy, query parameters)
  3. Anatomy of a Request & Response (interactive clickable packet explorer)
  4. The 4 Verbs (CRUD + `PUT` vs `PATCH`) & Status Code Traffic Light (`2xx`/`4xx`/`5xx`)
  5. Live Offline Interactive Playground (Mini Campus Pizza API with live in-memory database table, auth-key toggle, JSON editor, and guided crowd demos for `200`, `201`, `401`, `404`)
  6. API Design Principles Part 1 (URL & data craft: nouns vs verbs, plural consistency, honest status codes — interactive Good vs Bad flip cards)
  7. API Design Principles Part 2 (real-world engineering: statelessness, auth in headers never URLs, `/v1/` versioning, `429` rate limits)
  8. Interactive Challenge: "Code Review This Bad API" (4 realistic broken API snippets with instant feedback and score)
  9. Polling vs Webhooks (90-second pizza-buzzer visual planting the seed for Day 2 Labs 6–7) + bridge to Lab 1
- **Dual-Mode Presentation Experience (Option C)**: Add a scoped stylesheet (`docs/stylesheets/api-intro.css`) and local offline script (`docs/assets/javascripts/api-intro.js`) enabling **1-click Present Mode** (`Present Mode` button or `P` key, `ArrowLeft`/`ArrowRight`/`Esc` navigation, hidden MkDocs sidebars/header/instructor notes, projector-scaled typography, slide counter, and optional 30-minute pacing timer) while preserving the normal scrolling MkDocs study view by default.
- **Combine old Lab 0 + Lab 1 into Lab 1 (`docs/day2/lab1-rest.md`)**: Merge Bruno install, Python library install (`pip install`), Webex token setup (`token.txt` + `lab0/setup.py`), first live Webex Bruno call (`GET /v1/people/me`), "Break it on purpose" Bruno missions (`200`/`404`/`401`/`?max=2`), and Python `requests` (`lab1/get_rooms.py` `TODO 1`–`TODO 4`) into a streamlined 3-part **Lab 1 - Setup, Bruno & REST** (trimming the duplicate API-basics intro in favor of a pointer to Lab 0), and remove the superseded `docs/day2/lab0-setup.md`.
- **Update Day 2 navigation & cross-references**: Update `mkdocs.yml`, `docs/overrides/partials/progress-map.html` (keeping the 8-slot `Lab 0`–`Lab 7` bar: `Lab 0 API Basics`, `Lab 1 Setup & REST`), `docs/overrides/home.html` (`Start Day 2` -> `day2/lab0-api-basics.html`), `docs/day2/overview.md`, `docs/day2/lab7-fastapi.md`, and `docs/includes/abbreviations.md` (`endpoint`, `header`, `stateless`, `status code`).
- **Keep existing student code untouched**: Preserve all existing files under `code/day2/` (`lab0/setup.py`, `lab1/get_rooms.py`, `solutions/`, `bruno-collection/`), Day 1 pages/code, and existing `docs/stylesheets/{extra,callouts,fonts,print}.css`.

## Capabilities

### New Capabilities
- `day2-api-core-principles`: Interactive, projector-presentable 30-minute Day 2 Lab 0 teaching vendor-neutral API core principles and REST API design (with offline interactive playground, design code-review quiz, and dual-mode Present Mode), plus consolidated Day 2 Lab 1 setup/Bruno/REST flow.

### Modified Capabilities
<!-- None; no durable specs exist in openspec/specs/ yet. -->

## Impact

- **Docs**: Add `docs/day2/lab0-api-basics.md`; update `docs/day2/lab1-rest.md`, `docs/day2/overview.md`, `docs/day2/lab7-fastapi.md`, `docs/includes/abbreviations.md`; remove `docs/day2/lab0-setup.md`.
- **Theme / Config**: Update `mkdocs.yml` (nav + scoped extra CSS/JS), `docs/overrides/partials/progress-map.html`, `docs/overrides/home.html`.
- **Frontend assets (offline-safe)**: Add `docs/stylesheets/api-intro.css` and `docs/assets/javascripts/api-intro.js` (zero external URLs, strictly scoped to Lab 0 so Day 1 and other pages are unaffected).
- **Code & CI**: Zero changes to `code/day2/**/*.py`, `code/day2/bruno-collection/`, Day 1 files, or existing stylesheets; must pass `scripts/check_code.py`, `scripts/package.py` (0 external URLs), and `scripts/check_diagrams.py`.
