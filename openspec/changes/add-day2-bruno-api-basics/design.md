# Design

## Context

See `proposal.md` for motivation and scope. Day 2 (`docs/day2/` and `code/day2/`) is now merged locally and running on `http://127.0.0.1:8000/Cisco-Technology-Experience/`. `Bruno.exe` is installed on the workshop workstation (`C:\Users\mohamusa\AppData\Local\Programs\bruno\Bruno.exe`). Day 1 uses crisp ~1560px annotated screenshots (`docs/assets/screens/*.png`) with numbered red callouts (`1`, `2`, `3`) and sample student `Ola`, plus Mermaid diagrams with `color:#1b242c` on styled nodes so they remain legible in dark mode.

## Goals / Non-Goals

**Goals:**
- Keep Labs 0 and 1 **short and sweet**—visual, scannable, and interactive rather than prose-heavy.
- Give high school beginners an immediate "aha!" loop: see their own Webex profile JSON in Bruno (`GET /v1/people/me`), deliberately trigger `404` and `401` in Bruno, then see how Bruno's 3 fields become 3 lines of Python `requests.get()`.
- Produce crisp, legible, privacy-safe annotated Bruno screenshots matching Day 1's visual quality.
- Provide a 1-click fallback `code/day2/bruno-collection/` so no student gets stuck mistyping URLs.
- Keep everything 100% offline-compatible in `dist/python-workshop.zip` and verify locally before pushing.

**Non-Goals:**
- Calling external third-party public APIs (e.g., PokeAPI or weather APIs) that school/event Wi-Fi might block—stay strictly on `https://webexapis.com/v1/...`.
- Adding custom JavaScript widgets or modifying `docs/stylesheets/extra.css` (keep the site's existing styling and lightweight MkDocs Material components: Mermaid, tables, concept cards, `!!! predict` puzzles, tabs, and GLightbox zoomable screenshots).
- Modifying any Day 1 pages, Day 1 code, or existing Day 2 `.py` files.
- Committing or pushing to GitHub before the owner reviews the local preview.

## Decisions

### D1. Keep interactivity native to Bruno + MkDocs Material (no custom JS simulator)
- **Choice**: Make the lab genuinely interactive through **hands-on Bruno missions** ("Who am I?" + "Break It on Purpose": `200`, `404`, `401`, `?max=2") combined with **collapsible `!!! predict` "API Detective" puzzles**, **Mermaid flow diagrams**, and **zoomable annotated Bruno screenshots** (already supported by `glightbox`).
- **Alternatives considered**:
  - *Custom inline HTML/JS API simulator widget*: adds custom JS/CSS to maintain and risks clashing with light/dark mode or bloating the page when students are already installing Bruno on their laptops.

### D2. Capture/render crisp annotated Bruno screenshots modeled directly on real Bruno UI
- **Choice**: Create three annotated PNGs under `docs/assets/screens/` (~1560px wide, matching Day 1's exact red numbered callout badges and dark UI look):
  1. `bruno-auth-bearer.png`: Bruno's **Auth -> Bearer Token** tab showing where to paste the token (masked placeholder) with numbered callouts.
  2. `bruno-get-me.png`: Bruno sending `GET https://webexapis.com/v1/people/me` and receiving `200 OK` with sample student `Ola Nowak` JSON (`displayName`, `emails`, `nickName`), with callouts for Method, URL, Send, Status badge, and JSON body.
  3. `bruno-error-401.png`: Bruno showing a `401 Unauthorized` error response (and highlighting how to read the red status pill and error `message`) so students recognize errors immediately during "Break It on Purpose".
  We will inspect real `Bruno.exe` UI layout/colors (and/or capture from `Bruno.exe` with sample local mock/401 + annotate with numbered red callouts) so the screenshots accurately mirror what students see when they open Bruno, with zero real tokens or real user emails.
- **Alternatives considered**:
  - *Raw unannotated screenshots*: hard for high-school beginners to know which button to click in a dense API client window.
  - *Using a live personal Webex token during capture*: unacceptable privacy/security risk in a public repo.

### D3. Provide a 5-file plain-text Bruno collection in `code/day2/bruno-collection/`
- **Choice**: Ship a valid Bruno v1 collection folder:
  - `code/day2/bruno-collection/bruno.json`
  - `code/day2/bruno-collection/environments/Webex.bru` (`vars { token: PASTE_YOUR_TOKEN_HERE }`)
  - `code/day2/bruno-collection/Who am I.bru` (`GET https://webexapis.com/v1/people/me` with `auth:bearer { token: {{token}} }`)
  - `code/day2/bruno-collection/List rooms.bru` (`GET https://webexapis.com/v1/rooms?max=5` with `auth:bearer { token: {{token}} }`)
  - `code/day2/bruno-collection/Break it 404.bru` (`GET https://webexapis.com/v1/pizza` with `auth:bearer { token: {{token}} }`)
  Students are encouraged to create their first request from scratch in Lab 0 (takes 30 seconds), and can open `code/day2/bruno-collection` as a checkpoint if they fall behind—matching Day 1's "nobody gets left behind" pattern.
- **Alternatives considered**:
  - *No starter collection*: slower in a classroom if students mistype `webexapis.com` or forget `Bearer`.

### D4. Short-and-sweet structure across Lab 0 and Lab 1
- **Choice**:
  - **Lab 0**: Replace the thin 1-diagram opener with a punchy API intro (Mermaid everyday-apps diagram + 4-row `GET/POST/PUT/DELETE` table + 3-question "API Detective" `predict` card), add a compact "Install Bruno" step (Windows/Mac tabs, `usebruno.com/downloads`), keep `pip install` and `token.txt`, add step "Your first API call in Bruno (`GET /v1/people/me`)" with `bruno-auth-bearer.png` and `bruno-get-me.png`, then finish with `lab0/setup.py`.
  - **Lab 1**: Add a 3-node Status Code traffic-light Mermaid diagram (`2xx` / `4xx` / `5xx`), add step "Break It on Purpose in Bruno" (4 quick bullets: `/v1/rooms` -> `200`, `/v1/pizza` -> `404`, bad token -> `401`, `?max=2`) with `bruno-error-401.png`, add a **Bruno -> Python** Mermaid bridge diagram, then flow straight into the existing `TODO 1`–`TODO 4` Python steps (`rooms_sample.json` -> live `requests.get`).
- **Alternatives considered**:
  - *Creating a brand-new separate "Lab 0.5 - Bruno" page*: would change the 8-lab stepper (`Lab 0`–`Lab 7`) and break symmetry with Day 1.

## Risks / Trade-offs

- **Students cannot install Bruno on locked-down laptops** -> Mitigate with an instructor note in Lab 0 ("pair with a neighbour or follow the annotated screenshots; Lab 1's Python steps still work with `rooms_sample.json`").
- **Real token pasted into `environments/Webex.bru` during testing** -> Mitigate by warning students never to commit `Webex.bru` if they edit it, and in our repo keeping only `PASTE_YOUR_TOKEN_HERE` (verified before any commit).
- **Mermaid dark-mode readability** -> Mitigate by adding `color:#1b242c` on every styled node and checking all diagrams with `scripts/check_diagrams.py` and visual screenshots.
- **Cheat sheet overflowing 1 printed A4 page** -> Mitigate by keeping the 4-verb HTTP box ultra-compact (4 one-line rows) and verifying print layout.

## Migration Plan

1. Apply all changes locally (screenshots, `code/day2/bruno-collection/`, `docs/day2/{lab0-setup,lab1-rest,overview,cheat-sheet}.md`, `docs/includes/abbreviations.md`).
2. Run `scripts/check_code.py`, `scripts/package.py`, `scripts/check_diagrams.py`, and `git diff` boundary checks.
3. Verify visually in headless Edge and on the local `mkdocs serve` preview (`http://127.0.0.1:8000/Cisco-Technology-Experience/`).
4. Wait for owner approval before committing or pushing to `origin/main`.
