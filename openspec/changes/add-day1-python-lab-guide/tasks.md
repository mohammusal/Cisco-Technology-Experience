# Tasks

## 1. Authoring setup

- [x] 1.1 Create the project layout from design D1 (`docs/`, `docs/day1/`, `docs/day2/`, `docs/help/`, `docs/includes/`, `docs/overrides/partials/`, `docs/stylesheets/`, `docs/assets/`, `code/`, `scripts/`). Verify each folder exists.
- [x] 1.2 Add `requirements.txt` with the pinned versions from D11, create `.venv` and install it. Verify `mkdocs --version` prints 1.6.1.
- [x] 1.3 Add a `.gitignore` covering `.venv/`, `site/`, `dist/`, `__pycache__/` and `code/**/scores.txt`. Verify `git status` would not list those paths.

## 2. Site shell and Cisco styling

- [x] 2.1 Write `mkdocs.yml` with the following, and verify `mkdocs build --strict` succeeds:
  - the Material theme
  - the `offline` plugin
  - `use_directory_urls: false`
  - `theme.font: false`
  - no `navigation.instant`
  - the light and dark palette toggle
  - the markdown extensions from `cl_2026` (no Mermaid)
  - the Home / Day 1 / Day 2 / Help navigation
- [ ] 2.2 Copy the Cisco logo from `cl_2026` into `docs/assets/`, and set navy, cyan and link colours in one block of `docs/stylesheets/extra.css`. Verify in `mkdocs serve` that the header logo, tab icon and colours appear in both light and dark mode.
- [x] 2.3 Build the code-themed `overrides/home.html`, styled as a VS Code window, with a CSS typing effect, links to "Before you come", Lab 0 and the cheat sheet, and a `prefers-reduced-motion` fallback. Verify the page appears, and that with reduced motion on in the operating system the text shows without animation.
- [x] 2.4 Add the `docs/day2/index.md` placeholder page. Verify the Day 2 tab opens it.
- [x] 2.5 Add the author `README.md` covering install, `mkdocs serve` and packaging. Verify that following it in a fresh terminal starts the preview with live reload.

## 3. Beginner components

- [x] 3.1 Add `docs/stylesheets/callouts.css` with the custom admonitions `predict`, `checkpoint`, `error`, `analogy` and `badge`, using inline SVG icons (D4). Verify on a scratch page that each one appears with its own icon and colour, and that `???+ predict` stays collapsed.
- [x] 3.2 Add the concept-card grid and the lab summary strip CSS, adapted from `cl_2026`. Verify that at about 700 pixels wide the cards stack into one column without horizontal scrolling.
- [x] 3.3 Build the progress-map partial driven by the `lab:` front matter (D6), and hook it into the page template. Verify that on a page with `lab: 3`, Labs 0-2 show as done, Lab 3 as current, Labs 4-7 as upcoming, and every step links to its lab.
- [x] 3.4 Set up the glossary: `docs/includes/abbreviations.md`, auto-appended with snippets, and `docs/help/glossary.md` built from the same terms (D7). Verify that hovering "variable" on a lab page shows the tooltip, and that the glossary page lists the term.
- [x] 3.5 Write the lab page template (D9) as a commented example, `docs/includes/lab-template.md`, excluded from navigation. Verify it builds with no warnings and uses every component from 3.1-3.4.

## 4. Student code and Quiz Game

- [x] 4.1 Write `code/questions.py` with at least 15 short questions covering Kraków and Poland, tech and Cisco, Day 1 Python, and fun, with lowercase answers of one word or one number and no diacritics. Verify `python -c "from questions import QUESTIONS; print(len(QUESTIONS))"` prints 15 or more.
- [x] 4.2 Write `solutions/quiz_after_lab1.py` to `quiz_after_lab3.py` (greeting, Y/N start, one question asked until correct). Run each one by hand and verify it matches the Lab 1-3 behaviour in the `quiz-game-lab-code` spec, including the goodbye message on `n`.
- [x] 4.3 Write `solutions/quiz_after_lab4.py` and `quiz_after_lab5.py` (random pick, answers matched regardless of case and spaces, questions from the bank, a score). Verify that `  Warsaw ` is accepted as correct, and that a question newly added to `questions.py` can be picked without editing the game.
- [x] 4.4 Write `solutions/quiz_after_lab6.py`: the `ask_question()` function, re-prompting on invalid input, and appending `name,score` to `scores.txt` with a missing file handled. Verify that typing `maybe` at the Y/N prompt re-prompts, and that the first run with no `scores.txt` creates it.
- [x] 4.5 Write `solutions/quiz_final.py` (Lab 7): 5 questions picked with `random.sample` (no repeats), +1 or -1 scoring, the 30-second rule using `time.time()`, and the top 3 scores. Verify these by hand:
  - 3 right and 2 wrong answers give a score of 1
  - a correct answer after more than 30 seconds says "too slow" and adds 0
  - the top 3 scores list highest first
- [x] 4.6 Create `code/quiz.py` as the empty-start file for Lab 1. Write the practice starter files in `code/lab0/` to `code/lab7/` with numbered `# TODO N` markers, plus practice solutions in `code/solutions/`. Verify every starter and solution runs with `python <file>` without errors on Python 3.10 or newer.
- [x] 4.7 Add a small check script, `scripts/check_code.py`, that runs each solution with scripted input and checks key output lines. Verify it passes on Windows, and on macOS where available.

## 5. Day 1 content

- [x] 5.1 Write `docs/day1/schedule.md` with these slide ranges and times, and verify that the ranges cover slides 1-144 with no gaps, slide minutes total about 60, and lab minutes total about 300:

  | Slides | Minutes | Lab | Lab minutes |
  |---|---|---|---|
  | 1-19 | 10 | Lab 0 | 30 |
  | 20-28 | 7 | Lab 1 | 30 |
  | 29-42 | 8 | Lab 2 | 35 |
  | 43-54 | 6 | Lab 3 | 35 |
  | 55-105 | 13 | Lab 4 | 45 |
  | 106-117 | 5 | Lab 5 | 30 |
  | 118-141 | 9 | Lab 6 | 40 |
  | 142-144 | 2 | Lab 7 | 55 |

  Breaks are listed separately.
- [ ] 5.2 Write `docs/day1/before-you-come.md` with Windows and macOS tabs: install Python 3 (ticking "Add python.exe to PATH" shown on Windows, `python3` used on macOS), VS Code and the Python extension, then run `hello.py`. Include a screenshot for each key screen. Verify by following it on a clean Windows machine, and on macOS if available.
- [ ] 5.3 Write `docs/day1/lab0-setup.md`: the on-the-day check, opening the `code` folder in VS Code, and running `lab0/hello.py` to print `Hello World`. Verify that someone who did the pre-work can complete it in under 15 minutes.
- [x] 5.4 Write `docs/day1/lab1-variables.md` (slides 20-28) from the template, including its Quiz Game step (the greeting). Verify it builds strictly and has at least two Predict callouts, error decoders for `NameError` and `TypeError`, three-tab exercises, a checkpoint naming `quiz_after_lab1.py`, and a badge. Review it as the reference lab before continuing.
- [x] 5.5 Write `docs/day1/lab2-decisions.md` (slides 29-42). Its error decoders cover the missing colon (`SyntaxError: expected ':'`) and `IndentationError`. Verify the same checklist as 5.4.
- [x] 5.6 Write `docs/day1/lab3-loops.md` (slides 43-54), with a decoder for infinite loops (Ctrl+C). Add `docs/day1/break-1.md` (10 minutes) between Lab 0 and Lab 1. Verify the same checklist as 5.4, and that the break page appears in the navigation.
- [x] 5.7 Write `docs/day1/lab4-lists-strings.md` (slides 55-105), covering indexing, negative indexes, slicing, `append`, `del`, `index` and `remove`, plus the string methods `split`, `join`, `upper` and `lower`, `replace`, `startswith` and `in`. Decoders cover `IndexError`, `ValueError` and the string `TypeError` from item assignment. Verify the same checklist as 5.4.
- [x] 5.8 Write `docs/day1/lab5-collections.md` (slides 106-117). It covers tuples, dictionaries and sets, and states the correct dictionary facts (insertion order kept, lists cannot be keys, values can be any type), with a `KeyError` decoder. Add `docs/day1/break-2.md` (15 minutes) before Lab 6. Verify the same checklist as 5.4.
- [x] 5.9 Write `docs/day1/lab6-functions.md` (slides 118-141), covering `def`, `return`, positional and keyword arguments, `input()`, `open()` to read and write, and `try`/`except`/`finally`. Decoders cover `ZeroDivisionError`, `FileNotFoundError` and `ValueError` from `int()`. Verify the same checklist as 5.4.
- [x] 5.10 Write `docs/day1/lab7-quiz-game.md` (slides 142-144): put the game together, the 30-second rule, top scores, and Challenge ideas (categories, difficulty, adding school questions). Verify that following only the Follow along code gives a game whose behaviour matches `quiz_final.py`.
- [x] 5.11 Write `docs/day1/cheat-sheet.md` with one tiny example per concept from Labs 1-6, and a print stylesheet that hides navigation. Verify that printing to PDF in Edge or Chrome gives exactly one A4 page.
- [x] 5.12 Proofread all Day 1 pages for plain English: short sentences, every term defined or glossary-linked on first use, and no terms that the slides have not introduced. Verify by reading each page against the "Plain-language explanations" requirement, and fix any finds.

## 6. Help pages

- [ ] 6.1 Write `docs/help/troubleshooting.md`, with symptom and fix for each problem:
  - `python` opens the Microsoft Store
  - `python` not found or PATH not set
  - macOS `python` vs `python3`
  - VS Code using the wrong interpreter
  - the Run button not shown
  - the file not saved before running
  - running in the wrong folder

  Verify each fix on Windows, and on macOS where it applies.
- [x] 6.2 Add a "Still stuck?" section to `docs/help/troubleshooting.md` telling students to pair with a neighbour and call an instructor, with no browser-based editor mentioned anywhere (D12). Verify that a search of `docs/` finds no link to an online Python editor.

## 7. Packaging and end-to-end checks

- [x] 7.1 Write `scripts/package.py` (D10). It runs `mkdocs build --strict`, assembles `dist/python-workshop-day1/` with `START_HERE.html`, `guide/` and a clean `code/`, scans the HTML for external resource URLs (failing if any are found), and zips to `dist/python-workshop-day1.zip`. Verify that running it produces the ZIP and reports zero external URLs.
- [ ] 7.2 Test the handout offline. Unzip on Windows, turn Wi-Fi off, open `START_HERE.html` in Edge and Chrome, then click through every page and search for "loop". Verify every page, image and icon loads and search returns results. Repeat in Safari on macOS if available.
- [ ] 7.3 Run the dry run of the day. A tester with no Python experience follows "Before you come" and Labs 0-7 from the unzipped handout, recording minutes per lab. Verify the total is within about 300 minutes, the final game works, and every problem found is fixed in the guide or code.
