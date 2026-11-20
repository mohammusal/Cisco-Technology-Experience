# Cisco Technology Experience - Python Workshop lab guide

The lab guide for the Cisco Technology Experience Python workshop for high school students in Kraków
(slides 1-144, Python basics and the Quiz Game project).

The guide is an [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) site. Students
open it online at **<https://mohammusal.github.io/Cisco-Technology-Experience/>**, or from the
offline ZIP (`START_HERE.html`), which also holds the `code/` folder they work in.

## Set up (once)

You need Python 3.10 or newer.

```powershell
python -m venv .venv
.venv\Scripts\activate          # macOS / Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Preview while you write

```powershell
mkdocs serve
```

Open <http://127.0.0.1:8000>. The page reloads every time you save a file.

## Check before you commit

```powershell
mkdocs build --strict           # any warning fails the build
python scripts/check_code.py    # runs every starter and solution with scripted input
python scripts/check_diagrams.py  # parses every Mermaid diagram in site/ (Edge; set EDGE for another Chromium)
```

On Windows, if `check_code.py` prints garbled characters, run `$env:PYTHONIOENCODING = "utf-8"` first.

## Make the student handout

```powershell
python scripts/package.py
```

This builds the site, puts it together with the `code/` folder in
`dist/python-workshop/`, checks that no page loads anything from the internet, and writes
`dist/python-workshop.zip`. Hand out the ZIP (USB stick or download).

## Publish the guide online

The live guide is <https://mohammusal.github.io/Cisco-Technology-Experience/>. Share that link with
attendees. A link to one page works too, for example `.../day1/lab3-loops.html`.

**Pushing to `main` publishes.** The workflow `.github/workflows/pages.yml` then:

1. runs `scripts/check_code.py`,
2. runs `scripts/package.py` (strict build, and the check that nothing loads from the internet),
3. runs `scripts/check_diagrams.py` with Google Chrome,
4. publishes `site/` to GitHub Pages.

If any step fails, nothing is published and the live site stays as it was. Watch the runs in the
repository's **Actions** tab; a full run takes a few minutes. To republish without a new commit,
open **Actions > Publish the guide > Run workflow**.

**One-time setup** (repository owner): **Settings > Pages > Build and deployment > Source:
GitHub Actions**.

**Before you push**, run the same checks locally:

```powershell
python scripts/check_code.py
python scripts/package.py
python scripts/check_diagrams.py
git push
```

**Roll back** a bad change by reverting its commit and pushing:

```powershell
git revert HEAD
git push
```

To take the site offline completely, unpublish it under **Settings > Pages**.

## Where things are

| Path | What it is |
|---|---|
| `docs/day1/` | the workshop pages: roadmap, before you come, Labs 0-7, cheat sheet |
| `docs/help/` | troubleshooting and the glossary |
| `docs/includes/abbreviations.md` | glossary terms: shown as tooltips on every page and listed on the glossary page |
| `docs/includes/lab-template.md` | a commented example lab page: start every new lab from it |
| `docs/overrides/` | theme overrides: home page, file tab, progress map |
| `docs/stylesheets/` | Cisco colours, custom callouts, print layout for the cheat sheet |
| `hooks/glossary.py` | builds the glossary page from `abbreviations.md` |
| `code/` | the folder students open in VS Code: `quiz.py`, `questions.py`, `lab0/`-`lab7/`, `solutions/` |
| `scripts/` | `check_code.py`, `check_diagrams.py` and `package.py` |
| `docs/assets/javascripts/mermaid.min.js` | Mermaid 11.17.2 (MIT), bundled so diagrams work offline |
| `docs/assets/fonts/OFL.txt`, `docs/assets/javascripts/THIRD-PARTY-NOTICES.txt` | licences of the bundled fonts and scripts |
| `.github/workflows/pages.yml` | checks, builds and publishes the guide to GitHub Pages on every push to `main` |
| `openspec/` | the change proposal, design and specs this guide was built from |

## Writing rules

- Plain English for absolute beginners: short sentences, every new term explained or in the glossary.
- Every code block in the guide must run as shown, and every `Output` block must be real output.
- Solutions are included from `code/solutions/` with `--8<-- "code/solutions/file.py"`, never pasted.
- Everything happens in VS Code: do not link online Python editors.
- No external fonts, scripts or images: the guide must work with Wi-Fi off.
