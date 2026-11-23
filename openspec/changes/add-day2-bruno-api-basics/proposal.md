# Proposal

## Why

Day 2 currently jumps straight into `pip install`, copying a Webex token, and parsing `rooms_sample.json` in Python before high school beginners ever see an API respond visually. Introducing API basics in Day 2 Lab 0 and Lab 1 with **Bruno** (a free, no-account REST API client) and annotated screenshots gives students a short, interactive "See it -> Break it -> Code it" bridge against the Webex API before they write their first `requests.get()` call.

## What Changes

- **Upgrade Day 2 Lab 0 (`docs/day2/lab0-setup.md`)** with a short, visual API basics opener:
  - Everyday API hook (Mermaid diagram + compact 4-verb cheat table: `GET`, `POST`, `PUT`, `DELETE`).
  - Interactive "API Detective" quick-fire `predict` puzzle so students match everyday app actions to HTTP verbs.
  - Short Bruno installation step (Windows/Mac tabs, free, no account needed).
  - First live Webex API call in Bruno (`GET https://webexapis.com/v1/people/me` with Bearer token) so students see their own Webex profile returned as JSON, paired with annotated Bruno screenshots.
  - Keep existing `pip install`, `token.txt`, and `lab0/setup.py` steps intact.
- **Upgrade Day 2 Lab 1 (`docs/day2/lab1-rest.md`)** with an interactive Bruno-to-Python bridge:
  - Visual Status Code traffic-light diagram (`2xx`, `4xx`, `5xx`).
  - "Break It on Purpose" mini-missions in Bruno against Webex (`GET /v1/rooms` -> `200 OK`, `GET /v1/pizza` -> `404 Not Found`, broken token -> `401 Unauthorized`, bonus `?max=2` query param) paired with an annotated Bruno error screenshot.
  - A visual **Bruno -> Python** Mermaid bridge diagram mapping Bruno's `Method` + `URL` + `Bearer` fields 1-for-1 onto `requests.get(url, headers=headers)`.
  - Keep all existing Lab 1 Python steps (`TODO 1`–`TODO 4` on `rooms_sample.json` and live Webex) untouched.
- **Add annotated Bruno screenshots** under `docs/assets/screens/` (`bruno-auth-bearer.png`, `bruno-get-me.png`, `bruno-error-401.png`) styled consistently with Day 1's numbered-callout screenshots and containing zero real tokens or personal data.
- **Add a ready-to-open Bruno starter collection** under `code/day2/bruno-collection/` (`bruno.json`, `environments/Webex.bru` with placeholder token, `Who am I.bru`, `List rooms.bru`, `Break it 404.bru`) so students who fall behind can open the collection in one click without typing URLs.
- **Update Day 2 supporting pages minimally**:
  - `docs/day2/overview.md`: note Bruno in the Lab 0 and Lab 1 roadmap rows.
  - `docs/day2/cheat-sheet.md`: add a compact 4-verb HTTP methods box (`GET`, `POST`, `PUT`, `DELETE`) if it keeps the one-page print layout intact.
  - `docs/includes/abbreviations.md`: add `Bruno` (and `HTTP` if helpful) for hover tooltips and glossary.
- **Keep Day 1, existing styling, and Day 2 Python files untouched**: zero edits to `docs/day1/*`, `docs/stylesheets/*`, Day 1 `code/`, or existing Day 2 `.py` scripts, and preview everything locally before pushing.

## Capabilities

### New Capabilities
- `day2-bruno-api-basics`: Short, interactive high-school introduction to REST API basics in Day 2 Labs 0 and 1 using Bruno against the Webex API, annotated Bruno screenshots, and a 1-click starter Bruno collection.

### Modified Capabilities
<!-- None: existing Day 1 behavior and Day 2 Python scripts remain unchanged. -->

## Impact

- **Docs**: `docs/day2/lab0-setup.md`, `docs/day2/lab1-rest.md`, `docs/day2/overview.md`, `docs/day2/cheat-sheet.md`, `docs/includes/abbreviations.md`.
- **Visual Assets**: `docs/assets/screens/bruno-auth-bearer.png`, `docs/assets/screens/bruno-get-me.png`, `docs/assets/screens/bruno-error-401.png` (new).
- **Student Handout Code**: `code/day2/bruno-collection/` (5 small plain-text files, packaged automatically into `dist/python-workshop.zip`).
- **Build & Checks**: Must continue passing `mkdocs build --strict`, `scripts/check_code.py`, `scripts/package.py` (0 external URLs), and `scripts/check_diagrams.py` (all Mermaid diagrams parse cleanly and stay excluded from search snippets).
- **Untouched**: `docs/day1/*`, `docs/stylesheets/*`, all Day 1 code/solutions, all existing Day 2 `.py` files, and remote `origin/main` until owner reviews locally.
