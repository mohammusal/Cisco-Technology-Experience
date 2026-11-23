# Spec Delta

## Purpose

Provides a vendor-neutral, 30-minute interactive Day 2 Lab 0 teaching API core principles and REST API design with a built-in projector Present Mode, and consolidates Webex setup, Bruno practice, and first Python REST calls into Day 2 Lab 1.

## ADDED Requirements

### Requirement: Vendor-neutral 30-minute API core principles module in Day 2 Lab 0
Day 2 Lab 0 (`docs/day2/lab0-api-basics.md`) SHALL teach API core principles and REST API design for high-school graduates in approximately 30 minutes without referencing Webex anywhere in its teaching examples, using a single Campus Pizza / Cafe API domain (`/v1/menu`, `/v1/orders`) organized into 9 projector-sized beats.

#### Scenario: Student studies Lab 0 from top to bottom without Webex dependency
- **WHEN** a student opens `day2/lab0-api-basics.html`
- **THEN** the page teaches why APIs exist (client-contract-server-database boundary), resources and query parameters, request/response anatomy, CRUD verbs (`GET`, `POST`, `PUT`/`PATCH`, `DELETE`) and status-code families (`2xx`/`4xx`/`5xx`), REST design principles (nouns vs verbs, plural consistency, honest status codes, statelessness, headers-only auth, `/v1/` versioning, `429` rate limits), and Polling vs Webhooks (pizza-buzzer analogy) using Campus Pizza examples only

#### Scenario: Instructor notes guide 30-minute pacing without cluttering students
- **WHEN** a user views Lab 0 in normal study mode
- **THEN** each teaching beat includes a collapsed `instructor` callout with timing and talking prompts that remains collapsed by default

### Requirement: Interactive clickable Request/Response Anatomy Explorer
Lab 0 SHALL include an interactive offline Request/Response Anatomy Explorer allowing users to inspect each part of an HTTP request (Verb, URL/Query, Headers, JSON Body) and HTTP response (Status Code, Headers, JSON Body) with plain-English explanations.

#### Scenario: Selecting a packet segment explains its role
- **WHEN** the presenter or student clicks a segment such as `Authorization: Bearer ...` or `201 Created` in the anatomy explorer
- **THEN** the widget highlights that segment and displays its purpose and common beginner pitfall without requiring internet access

### Requirement: Offline Live Campus Pizza API Playground
Lab 0 SHALL embed a self-contained offline interactive API playground backed by an in-memory Campus Pizza database (`/v1/menu` and `/v1/orders`) where users send `GET`, `POST`, `PATCH`/`PUT`, and `DELETE` requests, toggle a Staff API key header, edit a JSON request body, and observe live HTTP status codes, JSON responses, and live database state changes.

#### Scenario: Creating an order updates the live database and returns 201 Created
- **WHEN** a user selects `POST` on `/v1/orders` with valid JSON (`item`, `customer`) and clicks Send
- **THEN** the playground returns status `201 Created` with the created JSON record and immediately appends the new row to the visible in-memory Orders table

#### Scenario: Protected endpoint without API key returns 401 Unauthorized
- **WHEN** a user sends `DELETE` on `/v1/menu/2` with the Staff API Key toggle turned off
- **THEN** the playground returns status `401 Unauthorized` with a JSON error message and leaves the Menu table unchanged

#### Scenario: Missing resource returns 404 Not Found and query params filter results
- **WHEN** a user sends `GET /v1/orders/999` or `GET /v1/menu?category=pizza`
- **THEN** `/v1/orders/999` returns `404 Not Found` and `/v1/menu?category=pizza` returns `200 OK` containing only matching pizza items

#### Scenario: Reset button restores the initial dataset for repeated demos
- **WHEN** a user clicks Reset Data in the playground
- **THEN** the in-memory Menu and Orders tables restore their initial seed rows cleanly

### Requirement: Interactive API Design Good-vs-Bad Cards and Code Review Challenge
Lab 0 SHALL provide interactive Good-vs-Bad design comparisons and a 4-question "Code Review This Bad API" challenge with immediate per-question feedback, rationale, and live score tracking.

#### Scenario: Answering a code review challenge gives immediate feedback
- **WHEN** a student or presenter selects an answer option on one of the 4 broken API snippets (verb-in-URL, `200 OK` masking an error, API key leaked in query string, or unversioned/inconsistent endpoint)
- **THEN** the widget immediately marks the selection correct or incorrect, explains the underlying API design principle, and updates the challenge score

### Requirement: Dual-Mode Projector Present Mode (Option C)
Lab 0 SHALL render as a standard scrolling MkDocs Material page by default and provide a 1-click **Present Mode** (button and `P` keyboard shortcut) that hides MkDocs navigation chrome and instructor notes, scales content for projector readability, and steps through the 9 beats one screen at a time using Next/Prev buttons or keyboard arrows (`ArrowRight`/`ArrowLeft`/`Esc`) while keeping all interactive widgets functional.

#### Scenario: Entering Present Mode switches to full-screen slide view
- **WHEN** the instructor clicks the Present Mode button or presses `P` (outside text inputs) on Lab 0
- **THEN** the header, left sidebar, right table of contents, footer, and instructor notes hide, only the active beat is shown centered at projector-friendly scale, and a compact bottom control bar displays Prev/Next buttons, slide index (`1 / 9`), an optional 30-minute timer toggle, and Exit

#### Scenario: Keyboard shortcuts stay safe while typing in playground inputs
- **WHEN** the user is focused inside a text input, textarea, or select inside the API Playground and presses `P`, `ArrowLeft`, or `ArrowRight`
- **THEN** Present Mode does not toggle or change slides so typing and editing JSON works normally

#### Scenario: Exiting Present Mode restores the normal guide view
- **WHEN** the user clicks Exit or presses `Esc` in Present Mode
- **THEN** the standard MkDocs scrolling page layout is fully restored

### Requirement: Consolidated Day 2 Lab 1 for Setup, Bruno, and First Python REST Calls
Day 2 Lab 1 (`docs/day2/lab1-rest.md`) SHALL combine the former Lab 0 setup steps (Bruno install, `pip install`, Webex token, `token.txt`, `lab0/setup.py`, and first live `GET /v1/people/me` call in Bruno) with the Lab 1 Bruno "Break it on purpose" experiments (`200`/`404`/`401`/`?max=2`) and Python `requests` steps (`lab1/get_rooms.py` `TODO 1`–`TODO 4`), linking back to Lab 0 for theory instead of duplicating it, and the superseded `docs/day2/lab0-setup.md` SHALL be removed.

#### Scenario: Student completes all Day 2 setup, Bruno, and first Python REST steps in Lab 1
- **WHEN** a student opens `day2/lab1-rest.html`
- **THEN** the page guides them sequentially through Part A (Bruno + Python packages + Webex token + `token.txt` + `lab0/setup.py`), Part B (live Webex calls and error experiments in Bruno using `code/day2/bruno-collection` and the 3 annotated Bruno screenshots), and Part C (translating Bruno to Python in `lab1/get_rooms.py` `TODO 1`–`TODO 4`)

### Requirement: Consistent Day 2 Navigation, Glossary, Offline Bundle, and Strict Boundaries
The MkDocs navigation, Day 2 progress bar (`Lab 0`–`Lab 7`), home page `Start Day 2` button, Day 2 roadmap, and glossary SHALL route seamlessly through the new Lab 0 and consolidated Lab 1, while preserving 0 external URLs in the offline bundle, valid Mermaid diagrams excluded from search, and zero edits to Day 1 files, existing stylesheets, or `code/day2/**/*.py`.

#### Scenario: All internal links, offline packaging, code checks, and diagram checks pass
- **WHEN** `scripts/check_code.py`, `scripts/package.py`, and `scripts/check_diagrams.py` are run after the change
- **THEN** all checks pass with `mkdocs build --strict` reporting 0 warnings, `package.py` reporting 0 external resource URLs, all Mermaid diagrams parsing cleanly with 0 Mermaid leaks in `search_index.json`, and `git diff` touching zero files under `docs/day1/`, Day 1 `code/`, existing `code/day2/`, or existing `docs/stylesheets/{extra,callouts,fonts,print}.css`
