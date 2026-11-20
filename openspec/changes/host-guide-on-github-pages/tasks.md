# Tasks

## 1. Owner decisions and GitHub settings

- [x] 1.1 Owner confirms with the event organisers that the Cisco-branded guide may be published on the personal account `mohammusal`; verify by recording the answer in this task line. **Answer (owner, 2026-11-20):** OK to publish, the guide contains no private Cisco data.
- [x] 1.2 Owner sets **Settings > Pages > Source: GitHub Actions** in `mohammusal/Cisco-Technology-Experience`; verify the Pages settings page shows "GitHub Actions" as the source

## 2. Build configuration

- [x] 2.1 Set `site_url: https://mohammusal.github.io/Cisco-Technology-Experience/` in `mkdocs.yml`; verify `mkdocs build --strict` passes and `site/sitemap.xml` lists absolute URLs under that address
- [x] 2.2 Make the internet check in `scripts/package.py` skip `<link rel="canonical">` and `rel="alternate"` tags while still failing on any other `<link href="https://...">`; verify `python scripts/package.py` reports 0 external resource URLs, and that a temporary page with an external stylesheet link makes it fail
- [x] 2.3 Add `docs/assets/fonts/OFL.txt` (SIL OFL 1.1 with the IBM Plex copyright line) and `docs/assets/javascripts/THIRD-PARTY-NOTICES.txt` (Mermaid 11.17.2 and iframe-worker 1.0.4, MIT, with copyright lines); verify both files appear in `site/` and in `dist/python-workshop/guide/` after `package.py`, and the strict build still passes

## 3. Repository setup

- [x] 3.1 Extend `.gitignore` with `code/**/notes.txt`, `code/**/temperatures.txt` and `.cache/`, and add `.gitattributes` (`* text=auto`; `*.png`, `*.woff2`, `*.zip` binary); verify `git status` after `git init` lists no build output, `.venv/` or generated lab files
- [x] 3.2 Run `git init -b main`, add the remote `https://github.com/mohammusal/Cisco-Technology-Experience.git`, and stage everything; verify `git status --short` shows `docs/`, `code/`, `hooks/`, `scripts/`, `openspec/`, `mkdocs.yml`, `requirements.txt`, `README.md` and nothing under `site/`, `dist/` or `.venv/`

## 4. Publishing workflow

- [x] 4.1 Add `.github/workflows/pages.yml` as in design D2: `push` to `main` and `workflow_dispatch` triggers, minimal permissions, `pages` concurrency group, `build` job (Python 3.13, `pip install -r requirements.txt`, `check_code.py`, `package.py`, `check_diagrams.py` with `EDGE` set to the runner's Chrome, upload `site/`) and a `deploy` job that needs `build`; verify the YAML parses and every step command runs locally on Windows
- [x] 4.2 Add a "Publish the guide online" section to `README.md` covering the live link, the one-time Pages setting, "push to `main` publishes", the checks that run, and how to roll back; verify each command in the section runs as written

## 5. First publish and checks

- [x] 5.1 Check the remote with `git ls-remote origin`; if it has commits, fetch and rebase onto them. Then commit and `git push -u origin main` with the owner's credentials; verify the commit is visible on GitHub
- [x] 5.2 Watch the first run in the **Actions** tab; verify both jobs succeed and the `github-pages` environment shows the deployed address
- [x] 5.3 Open `https://mohammusal.github.io/Cisco-Technology-Experience/` on a desktop browser and a phone; verify the home page, Lab 3 opened directly from its own link, a screenshot, a Mermaid diagram and search all work, and the network inspector shows no requests to other sites
- [x] 5.4 Push a deliberately broken internal link on a test commit; verify the workflow fails, the live site is unchanged, then revert the commit and verify the next run publishes again

## Workflow follow-up

- Share the link with attendees next to the ZIP, for example as a QR code on the first slide.
- Archive this change once the site is live and checked.
- Separately, bring the older `add-day1-python-lab-guide` artifacts up to date (no Day 2, no timings, Mermaid allowed), since they are now public.
