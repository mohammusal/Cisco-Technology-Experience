# Spec Delta

## Purpose

Teaches high-school beginners REST API fundamentals in Day 2 Labs 0 and 1 through a concise, interactive "See it -> Break it -> Code it" sequence using Bruno against the Webex API, backed by annotated screenshots and a 1-click starter collection.

## ADDED Requirements

### Requirement: Day 2 Lab 0 introduces API basics and a first live Webex call in Bruno
Day 2 Lab 0 SHALL teach core API concepts (`GET`, `POST`, `PUT`, `DELETE`, URL, request/response) concisely with an interactive verb-matching puzzle, guide students to install Bruno on Windows or macOS, and walk them through calling `GET https://webexapis.com/v1/people/me` with a Bearer token in Bruno before running `lab0/setup.py`.

#### Scenario: Student completes the API basics hook and first Bruno request
- **WHEN** a reader opens `day2/lab0-setup.html`
- **THEN** the page presents a short everyday API diagram, a 4-verb cheat table (`GET`/`POST`/`PUT`/`DELETE`), an interactive collapsible "API Detective" `predict` puzzle, Windows/Mac Bruno installation steps, step-by-step Bearer auth + `GET https://webexapis.com/v1/people/me` instructions with annotated Bruno screenshots, and the existing `token.txt` and `lab0/setup.py` steps

#### Scenario: Webex-only scope with no external third-party APIs
- **WHEN** a student follows Labs 0 and 1
- **THEN** every live API call targets `https://webexapis.com/v1/...` with no reliance on third-party public APIs

### Requirement: Day 2 Lab 1 connects Bruno experiments to Python requests
Day 2 Lab 1 SHALL include a visual status-code traffic-light guide, hands-on "Break It on Purpose" mini-missions in Bruno (`200 OK` on `/v1/rooms`, `404 Not Found` on `/v1/pizza`, `401 Unauthorized` on a broken token, and `?max=2`), and a visual Bruno-to-Python mapping diagram leading into the existing `lab1/get_rooms.py` steps.

#### Scenario: Student experiments with status codes in Bruno before coding
- **WHEN** a reader opens `day2/lab1-rest.html`
- **THEN** the page displays a status-code diagram (`2xx`/`4xx`/`5xx`), the "Break It on Purpose" Bruno missions with an annotated error screenshot, a Bruno-to-Python bridge diagram mapping `GET` + URL + Bearer header to `requests.get()`, and all existing `TODO 1`–`TODO 4` Python steps intact

### Requirement: Annotated Bruno screenshots match the guide's visual standard and protect privacy
The guide SHALL bundle local annotated PNG screenshots under `docs/assets/screens/` illustrating Bearer token entry, a `200 OK` response on `/v1/people/me`, and a `401`/`404` error response in Bruno, containing zero real Webex tokens or personal attendee data.

#### Scenario: Screenshots load locally and remain offline-safe
- **WHEN** `scripts/package.py` builds the site and offline handout
- **THEN** `bruno-auth-bearer.png`, `bruno-get-me.png`, and `bruno-error-401.png` exist in `site/assets/screens/` and `dist/python-workshop/guide/assets/screens/`, contain only placeholder/sample student data (`Ola`), and `package.py` reports 0 external resource URLs

### Requirement: Ready-to-open Bruno starter collection is included in Day 2 code
The student code folder SHALL include a valid, plain-text Bruno collection under `code/day2/bruno-collection/` with placeholder token configuration so students can open the Lab 0 and Lab 1 requests in one click.

#### Scenario: Bruno collection is packaged without real secrets
- **WHEN** `scripts/package.py` assembles `dist/python-workshop/`
- **THEN** `dist/python-workshop/code/day2/bruno-collection/` contains `bruno.json`, `environments/Webex.bru` (with `PASTE_YOUR_TOKEN_HERE` only), `Who am I.bru`, `List rooms.bru`, and `Break it 404.bru`, with no real tokens committed or zipped

### Requirement: Day 2 overview, cheat sheet, and glossary reflect Bruno cleanly
The Day 2 roadmap, cheat sheet, and glossary SHALL reference Bruno and HTTP methods concisely without breaking the cheat sheet's compact layout or modifying Day 1 content.

#### Scenario: Supporting pages stay concise and build strictly
- **WHEN** `mkdocs build --strict` and `scripts/check_diagrams.py` run
- **THEN** `day2/overview.html` mentions Bruno in Labs 0–1, `day2/cheat-sheet.html` includes the 4 HTTP verbs, `help/glossary.html` defines `Bruno` and `HTTP`, and every Mermaid diagram across Day 1 and Day 2 parses cleanly with `data-search-exclude`

### Requirement: Day 1, existing CSS, and Day 2 Python scripts stay untouched
Adding the Bruno API basics experience MUST NOT alter any Day 1 page, Day 1 student file, CSS stylesheet, or existing Day 2 `.py` script, and MUST be previewed locally before any remote push.

#### Scenario: Boundary check confirms untouched files
- **WHEN** `git diff` is inspected after applying this change
- **THEN** zero files under `docs/day1/`, `docs/stylesheets/`, Day 1 `code/`, or existing `code/day2/**/*.py` are modified, and all checks in `scripts/check_code.py` continue to pass
