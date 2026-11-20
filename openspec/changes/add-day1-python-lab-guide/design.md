# Design

## Context

See proposal.md for motivation, and the three specs for the required behaviour.

The project is empty apart from `openspec/`. Two existing guides on this machine are the reference style:

- `C:\WorkRelated_LocalFiles\cl_2026\lab-guide`
  - MkDocs 1.6.1 and Material 9.8.0
  - `custom_dir` overrides with a custom `home.html`
  - custom admonition CSS
  - a phase bar, concept cards and Explorer/Builder/Engineer tabs
  - `pymdownx.snippets` with an auto-appended glossary
- `C:\WorkRelated_LocalFiles\wx1Simple\LAB-31123`
  - the same Material setup in a simpler form

Constraints that shape the approach:

- **Offline from `file://`:** students open the guide from an unzipped folder with no network.
- **Network-dependent parts of `cl_2026`:**
  - Font Awesome is imported from a CDN.
  - Material loads Google Fonts by default.
  - Mermaid would load from a CDN.
  - `navigation.instant` breaks on `file://`.
  - The home page uses a 39 MB GIF.
- **Beginners in VS Code:** students keep the guide beside VS Code, so pages must work at about half a laptop screen wide.
- **No Python tooling on the author machine yet:** `mkdocs-material` is not installed.

## Goals / Non-Goals

**Goals:**
- Reuse the `cl_2026` structure and look where it works offline, so the guide reads as a Cisco lab.
- Use one page template for every lab, so the eight labs stay consistent and quick to write.
- Make one build that works both from `mkdocs serve` and from an unzipped handout, and can be hosted later unchanged.
- Keep the student code tiny, readable and standard-library only.

**Non-Goals:**
- Hosting, CI or a GitHub Pages workflow.
- Translations.
- Grading students' code automatically or tracking their progress anywhere other than their own laptop.
- Real-time countdown timers or other concurrency in the Quiz Game.

## Decisions

### D1. Project layout

```
School Project/
+-- mkdocs.yml
+-- requirements.txt            pinned authoring tools
+-- README.md                   author instructions: install, serve, build, package
+-- docs/
|   +-- index.md                uses the home.html override
|   +-- day1/
|   |   +-- schedule.md
|   |   +-- before-you-come.md
|   |   +-- lab0-setup.md ... lab7-quiz-game.md
|   |   +-- break-1.md, break-2.md
|   |   +-- cheat-sheet.md
|   +-- day2/index.md           placeholder
|   +-- help/
|   |   +-- troubleshooting.md
|   |   +-- glossary.md
|   +-- includes/
|   |   +-- abbreviations.md    glossary tooltips, auto-appended
|   +-- overrides/
|   |   +-- home.html
|   |   +-- partials/           progress map partial
|   +-- stylesheets/
|   |   +-- extra.css, callouts.css
|   +-- assets/
|       +-- cisco_logo.png
|       +-- screenshots/
|       +-- fonts/ (if needed)
+-- code/                       copied into the handout as-is
|   +-- lab0/ ... lab7/
|   +-- quiz.py
|   +-- questions.py
|   +-- solutions/
+-- scripts/
    +-- package.py              build + assemble + zip
```

The site source and the student code sit side by side. The guide shows code by including the real files with `pymdownx.snippets`, so the code shown in the guide is the same code students run. *Alternative:* code pasted directly into the pages. That is rejected because the two would drift apart.

### D2. Offline-first MkDocs configuration

- **Material `offline` plugin:** keeps search working from `file://` and switches off features that need a server.
- **`use_directory_urls: false`:** links go to `page.html` and not to `page/`, so they work without a server.
- **No `navigation.instant`:** it does not work from `file://`.
- **Fonts:** `theme.font: false`, with the system font stack. This avoids Google Fonts and needs no font files. *Alternative:* self-hosted CiscoSans. That is rejected because licensing is unclear and it adds weight.
- **Icons:** only Material's bundled icon sets (`:material-*:` and `:octicons-*:`), including inline SVG icons for callouts. The Font Awesome CDN import in `cl_2026` is removed.
- **Diagrams:** no Mermaid. Diagrams are ASCII art in code blocks or small SVG files in `assets/`.
- **Home page:** the 39 MB GIF is replaced by a CSS gradient and a typing effect, with `prefers-reduced-motion` respected.

*Alternative:* asking students to run `mkdocs serve` themselves. That is rejected because it is too much setup for complete beginners.

### D3. Cisco styling

`extra.css` sets these values in one block, so a programme logo or colours can be swapped later:

- primary colour `#051C2C` (navy)
- accent colour `#00bdeb` (cyan)
- link colour `#3a7fff`

These are the same values as `cl_2026`, and the Cisco logo is copied from there. Light and dark schemes use the same palette toggle as `cl_2026`.

The slides' code-file look appears in three places:

- page titles carry a small "file tab" label such as `lab1_variables.py`
- section headers use the slides' `Name{ }` style on lab title cards
- the home page is a VS Code-like window

### D4. Beginner callouts as custom admonitions

Each callout is a custom admonition with an SVG icon set through `--md-admonition-icon--<name>`, the same technique as `cl_2026/admonition.css`.

| Callout | Used for | Rendering |
|---|---|---|
| `predict` | Guess, then reveal | `???` collapsible, so the answer stays hidden |
| `checkpoint` | Expected result plus catch-up file | Always open |
| `error` | Error decoder | Open, with a red accent and a fixed layout: message, meaning, fix |
| `analogy` | Everyday comparison | Inside concept cards |
| `tip` | VS Code shortcut or pro tip | Uses the built-in `tip` |
| `badge` | End-of-lab reward | Centred, with the lab colour |

Concept cards reuse the `cl_2026` `.concepts` grid CSS, which already stacks to one column on narrow windows.

### D5. Difficulty tabs

These use `pymdownx.tabbed` with `alternate_style` and `content.tabs.link`, as `cl_2026` does. The tab labels are always "Follow along", "Try it" and "Challenge", so choosing a level once switches every tab on the page to it. The Quiz Game step at the end of each lab sits outside the tabs and always gives the full code, so every student finishes each game step.

### D6. Progress map

A Jinja partial in `overrides/` draws the map from the page's `meta.lab` number (front matter `lab: 3`). It is the `cl_2026` `.lifecycle` bar widened to eight steps, with done, current and upcoming states. *Alternative:* a `macros` call on every page. That is rejected because front matter alone is simpler for authors.

The map also links to the previous and next labs. Material's footer navigation stays on.

### D7. Glossary tooltips

These use `abbr` and `pymdownx.snippets` `auto_append` of `includes/abbreviations.md`, as `cl_2026` does. The `glossary.md` page lists the same terms in full. One source file holds the term list, so the tooltips and the page cannot drift.

### D8. Quiz Game code design

The Quiz Game is a single `quiz.py` that grows. Each lab adds a clearly commented block, `# --- Lab N: <feature> ---`. Students edit their own `quiz.py`, and `solutions/quiz_after_labN.py` holds the state after each lab.

Logic stays at beginner level:

- **Labs 1-5:** no functions, so the code reads from top to bottom.
- **Lab 6:** the question logic is moved into `ask_question(question, answer)`. This shows why functions help, as slides 121-125 do.
- **Lab 6 file handling:** `scores.txt` holds lines in the form `name,score`. Reading uses `try/except FileNotFoundError`, which practises the exceptions part of slides 132-140.
- **Lab 7 timing:** `time.time()` before and after `input()`. If more than 30 seconds pass, the answer scores zero points. *Alternative:* `threading` or `signal` for a live countdown. That is rejected because it is beyond Day 1 and behaves differently on Windows and macOS.
- **Lab 7 question picking:** `random.sample` picks 5 different questions.

`questions.py` holds one dictionary of the form `QUESTIONS = {"What river flows through Krakow?": "vistula", ...}`, loaded with `from questions import QUESTIONS`. Answers are stored in lowercase and compared after `.strip().lower()`. Diacritics are avoided in answers ("krakow" and "lodz" are both accepted), because students may not have a Polish keyboard layout.

Labs 4 and 5 practise lists and dictionaries in their own starter files before they are used in the game. That keeps the new concept apart from the game code.

### D9. Lab page template

Each lab page follows the same order:

1. Front matter: `lab: N`, title and time.
2. Progress map (automatic).
3. A summary strip: time, "You build", slides.
4. Concept cards with analogies.
5. Steps (`### Step N.M`), each with an explanation, code (from a snippet), a run instruction and the expected output.
6. Predict, Error decoder and Tip callouts placed inside the steps.
7. Practice exercises in the three tabs.
8. "Add it to your Quiz Game".
9. Checkpoint.
10. Badge.

Lab 1 is written first and reviewed as the reference before Labs 2-7.

### D10. Packaging script

`scripts/package.py` is plain Python. It:

1. runs `mkdocs build --strict` into `site/`
2. assembles `dist/python-workshop-day1/` with `guide/` (the built site), `code/` (without `scores.txt` and `__pycache__`) and `START_HERE.html`
3. zips the result to `dist/python-workshop-day1.zip`

`START_HERE.html` is a tiny page with a meta refresh and a link to `guide/index.html`.

`--strict` makes broken links and missing snippets fail the build. The script can then scan the built HTML for `http://` and `https://` in `src=` and `href=` attributes that load resources, and stop if it finds any.

### D11. Authoring tools

`requirements.txt` pins the `cl_2026` versions:

- `mkdocs==1.6.1`
- `mkdocs-material==9.8.0`
- `mkdocs-glightbox==0.5.3`
- `mkdocs-macros-plugin==1.5.0`
- `pymdown-extensions==12.3`
- `Pygments==2.21.0`

The git-sourced `pygments-ios` dependency is dropped. Authors install these into a local `.venv`. The `README.md` documents the steps: create the venv, install, run `mkdocs serve`, run `python scripts/package.py`.

### D12. No browser-based Python fallback

All coding happens in VS Code with a local Python install. There is no browser-based Python editor. A student whose laptop cannot run Python pairs with a neighbour, and the troubleshooting page says so. *Alternative:* an online Python editor. That is rejected because the organisers decided not to use one.

## Risks / Trade-offs

- **[Risk]** Venue laptops are blocked from installing Python, or a student skips the pre-work. → **Mitigation:** the pre-work is sent days ahead, Lab 0 has 30 minutes on the schedule and needs only about 15 when the pre-work is done, and a student who still cannot run Python pairs with a neighbour.
- **[Risk]** The Material `offline` plugin can't search on some browsers from `file://`. → **Mitigation:** test the ZIP in Edge, Chrome and Safari before the event. Search is a convenience, because navigation alone covers every page.
- **[Risk]** Typing errors by beginners take up lab time. → **Mitigation:** short steps, copy buttons, error decoders at the points where beginners usually fail, and catch-up solutions after every lab.
- **[Risk]** 300 minutes is too much or too little for the class. → **Mitigation:** the Challenge tabs absorb extra time, and the Follow along tabs let a slow group keep up. Lab 7 can be cut to the 30-second rule only if time is short.
- **[Trade-off]** Without Mermaid and web fonts, the guide is a little less polished. In return it works anywhere with no network.
- **[Trade-off]** One growing `quiz.py` means a broken file blocks the next lab. → **Mitigation:** each checkpoint names the solution file to copy.

## Migration Plan

There is no existing content to migrate. Before the event:

1. Build and package.
2. Test the ZIP offline on Windows and macOS.
3. Send the "Before you come" page as a PDF or link with the pre-work message.
4. Bring the ZIP on USB sticks as a backup.

Hosting later means publishing the same `site/` folder, which needs no change.
