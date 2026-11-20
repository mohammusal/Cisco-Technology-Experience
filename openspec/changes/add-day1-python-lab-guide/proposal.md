# Proposal

## Why

The Cisco Technology Experience Python workshop in Kraków gives high school students about 6 hours of teaching on Day 1, but the only material is a 144-slide deck. Students have almost no programming experience, so they need 5 of those hours to be hands-on with a guide they can follow alone in VS Code, while the slides shrink to about 1 hour of short blocks between labs.

## What Changes

- Add an English MkDocs Material lab guide for Day 1 (slides 1-144), styled in Cisco colours and logo and echoing the slides' code-file look (`workshop.py`, `Variables{ }`).
- Organise Day 1 as alternating slide blocks (about 60 minutes total) and eight labs (about 300 minutes total, breaks extra):
  - Lab 0 Setup (pre-work plus an on-the-day check)
  - Lab 1 Variables, types and operators
  - Lab 2 Decisions (if/elif/else)
  - Lab 3 Loops
  - Lab 4 Lists and strings
  - Lab 5 Tuple, dictionary and set
  - Lab 6 Functions, files and exceptions
  - Lab 7 Quiz Game project
- Build the slide 144 Quiz Game step by step: each lab ends by adding one piece, and Lab 7 completes it. The 30-second rule is checked after each answer rather than with a live countdown.
- Write for complete beginners:
  - one concept per step
  - an everyday analogy for each concept
  - expected output for every run
  - "predict", "checkpoint" and "error decoder" callouts
  - three difficulty tabs per exercise (Follow along, Try it, Challenge)
  - a badge at the end of each lab
  - glossary tooltips
  - a printable cheat sheet
- Provide setup guidance for Windows and macOS and a troubleshooting page. All coding happens in VS Code; there is no browser-based Python editor, and students whose laptop cannot run Python pair with a neighbour.
- Provide starter files for each lab, a solution after each lab for catching up, and a simple question bank (about 15-20 questions) in its own file.
- Run the guide locally with `mkdocs serve` while writing. Hand it out to students as an offline ZIP (built site plus code) that opens from `index.html` with no network. The same build can be hosted later.
- Add a placeholder Day 2 tab so APIs and Webex content can be added later without restructuring.

Out of scope: Day 2 content, hosting, and corrections to the slide deck.

## Capabilities

### New Capabilities

- `lab-guide-site`: the MkDocs site itself. Covers Cisco styling and home page, navigation (Day 1 tab, Day 2 placeholder, help), beginner callouts and components, local preview, and the offline ZIP handout that works from `file://`.
- `python-day1-labs`: the Day 1 learning content. Covers the slide-to-lab schedule and timings, Lab 0 setup per operating system, Labs 1-7 with their exercises, difficulty tabs, checkpoints, error decoders, badges, glossary, cheat sheet and troubleshooting.
- `quiz-game-lab-code`: the code students work with. Covers starter files per lab, solutions after each lab, the step-by-step Quiz Game, the separate question bank, and the after-answer timing rule.

### Modified Capabilities

None. The project has no existing specs.

## Impact

- New site source in this project (MkDocs config, `docs/` pages, stylesheets and assets). The Cisco logo and styling approach are reused from the `cl_2026` lab guide.
- New student code folder (starter files, solutions, question bank) in plain Python using only the standard library (`random`, `time`).
- Authoring tools: Python with `mkdocs-material` and the plugins it needs (for example macros and glightbox). Everything runs offline, so the guide does not load fonts, icons or diagram libraries from the internet.
- Students need Python 3 and VS Code with the Python extension on their own laptops. Nothing has to be installed on the instructor's network.
- Facilitators get a pre-work message for students and a build-and-zip step before the event.
