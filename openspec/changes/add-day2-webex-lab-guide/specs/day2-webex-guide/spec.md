# Spec Delta

## Purpose

Adds the Day 2 Webex APIs workshop track—guide pages, student code, dual-day navigation, token leak safeguards, and offline code checks—to the MkDocs workshop site and offline student handout without modifying Day 1 or the existing visual styling.

## ADDED Requirements

### Requirement: Day 2 Webex APIs guide pages build cleanly
The site SHALL include all 10 Day 2 Markdown pages under `docs/day2/` (`overview.md`, `lab0-setup.md` through `lab7-fastapi.md`, and `cheat-sheet.md`) using the workshop's existing layout components, admonitions, tabs, and Mermaid diagrams.

#### Scenario: Strict MkDocs build succeeds with Day 2 pages
- **WHEN** `mkdocs build --strict` runs
- **THEN** the build exits with status 0 and emits all 10 HTML pages under `site/day2/` with no broken internal links or warnings

#### Scenario: All Day 2 Mermaid diagrams render and stay out of search snippets
- **WHEN** `scripts/check_diagrams.py` runs on the built site
- **THEN** all 14 Day 2 Mermaid diagrams (in addition to all 63 Day 1 diagrams) parse without errors and carry `data-search-exclude` so raw Mermaid source does not appear in search previews

#### Scenario: Offline handout stays free of internet dependencies
- **WHEN** `scripts/package.py` builds the offline bundle
- **THEN** the external-resource check reports 0 external resource URLs across both Day 1 and Day 2 pages

### Requirement: Day 2 student code and solutions are packaged intact
The repository SHALL include all 25 Day 2 student starter, helper, data, and solution files under `code/day2/` and package them into the offline handout ZIP.

#### Scenario: Student files appear in the repository and handout
- **WHEN** `scripts/package.py` assembles `dist/python-workshop/`
- **THEN** `dist/python-workshop/code/day2/` contains `config.py`, `webex_project.py`, `rooms_sample.json`, `token.example.txt`, `lab0/` through `lab7/`, and `solutions/`

### Requirement: Dual-day navigation and progress stepper
The site SHALL expose Day 2 via a top-level **Webex APIs** tab, home page entry points, and a Day 2 lab progress bar without altering Day 1 navigation or Day 1's progress bar.

#### Scenario: Home page links directly to Day 1 and Day 2
- **WHEN** a reader opens the home page
- **THEN** they can jump directly to Day 1 (`day1/lab0-setup.html`, `day1/overview.html`) or Day 2 (`day2/lab0-setup.html`, `day2/overview.html`) using the existing home page styling

#### Scenario: Progress bar adapts per day
- **WHEN** a reader opens any Day 2 lab page (`day: 2`, `lab: 0..7`)
- **THEN** the top progress bar displays the 8 Day 2 steps (`Token`, `REST`, `Room`, `Members`, `Messages`, `Bots`, `Flask`, `FastAPI`) with the active lab highlighted, while Day 1 lab pages continue to display the 8 Day 1 steps unchanged

### Requirement: Shared Help pages cover Day 2 topics
The Troubleshooting and Glossary pages SHALL include the Day 2 troubleshooting guidance and terminology alongside existing Day 1 entries.

#### Scenario: Day 2 troubleshooting items are searchable and visible
- **WHEN** a reader opens `help/troubleshooting.html`
- **THEN** the page includes sections for `Webex returns 401 Unauthorized`, `Webex returns 409 Conflict`, and `Flask or uvicorn cannot start` alongside all existing Day 1 sections

#### Scenario: Day 2 glossary terms populate tooltips and the glossary page
- **WHEN** the site is built
- **THEN** `help/glossary.html` and hover tooltips include `API`, `bot`, `FastAPI`, `Flask`, `JSON`, `REST`, `SDK`, `token`, and `webhook`

### Requirement: Webex access tokens are never committed or zipped
The repository and packaging script MUST exclude any real `token.txt` file while keeping `token.example.txt` tracked and packaged.

#### Scenario: Local token.txt is ignored by Git and packaging
- **WHEN** a real `code/day2/token.txt` file exists locally
- **THEN** `git status` does not list `code/day2/token.txt` and `scripts/package.py` omits `token.txt` from `dist/python-workshop/code/day2/` while still including `token.example.txt`

### Requirement: Offline automated verification for Day 2 code
The code verification script SHALL validate Day 2 student files offline without making network calls or requiring a Webex token, while preserving all existing Day 1 checks.

#### Scenario: Offline labs run and online labs pass syntax verification
- **WHEN** `python scripts/check_code.py` runs in a clean environment without `token.txt` or third-party Day 2 packages installed
- **THEN** all existing Day 1 checks pass, Day 2 `lab0` and `lab1` starters and solutions run against `rooms_sample.json` with expected output, `config.py` exits with its clear setup message when `token.txt` is absent, and all remaining Day 2 Python files (`lab2`–`lab7`, `webex_project.py`, and `solutions/`) parse with zero Python syntax errors

### Requirement: Day 1 content and site visual styling remain untouched
Merging Day 2 MUST NOT modify any Day 1 guide page, Day 1 student code or solution file, or the site's existing CSS stylesheets.

#### Scenario: Diff check confirms Day 1 and stylesheets are unchanged
- **WHEN** `git diff` is inspected after applying the change
- **THEN** zero files under `docs/day1/`, `docs/stylesheets/`, `code/lab0`–`code/lab7`, `code/quiz.py`, `code/questions.py`, or `code/solutions/` are modified

### Requirement: Local preview precedes any remote push
The merged Day 1 + Day 2 site MUST be verified locally with a live local preview server before any changes are committed or pushed to GitHub.

#### Scenario: Owner inspects combined guide locally first
- **WHEN** implementation and automated checks complete
- **THEN** the combined site is served locally via `mkdocs serve` and no commits are pushed to `origin/main` until the owner explicitly approves
