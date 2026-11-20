# Design

## Context

See proposal.md for why. The current state:

- The project folder is not a git repository yet. The GitHub repository exists, is public, and looks
  empty, but its contents could not be confirmed from the authoring network: the GitHub API returned 403.
- `scripts/package.py` already runs `python -m mkdocs build --strict --clean` into `site/`, then
  copies `site/` into `dist/python-workshop/guide/`, scans every HTML and CSS file for resources
  loaded from the internet, and zips the result. `site/` is left in place afterwards.
- `scripts/check_code.py` runs every starter and solution with scripted input.
  `scripts/check_diagrams.py` parses every Mermaid diagram with a headless Chromium browser. The
  browser path comes from the `EDGE` environment variable.
- `mkdocs.yml` uses the `offline` plugin, `use_directory_urls: false`, local fonts, a local Mermaid
  copy and a local iframe-worker shim. Nothing loads from other sites.
- `.gitignore` already excludes `.venv/`, `site/`, `dist/`, `__pycache__/`, `*.pyc` and `scores.txt`.
- Authors work on Windows with Python 3.14 in `.venv`. `requirements.txt` pins MkDocs 1.6.1,
  Material 9.8.0 and the plugins.

## Goals / Non-Goals

**Goals:**

- One workflow file that checks, builds and publishes. No publishing from a laptop.
- The hosted site and the ZIP come from the same build, and the ZIP's internet check keeps passing.

**Non-Goals:**

- Preview sites for pull requests, a custom domain, analytics, or a cookie banner.
- Publishing the ZIP as a GitHub Release. The organisers share it through the group.

## Decisions

### D1. Publish with GitHub Actions, not a `gh-pages` branch

The workflow uses GitHub's official Pages actions: `actions/configure-pages`,
`actions/upload-pages-artifact` with `site/`, and `actions/deploy-pages`. Pages is set to
**Source: GitHub Actions**.

*Alternative:* `mkdocs gh-deploy` from a laptop, which pushes to a `gh-pages` branch. Rejected:
publishing would depend on one person's laptop, nothing would run the checks, and the repository
would carry a branch of generated HTML.

### D2. The workflow: two jobs, `build` then `deploy`

- **Triggers:** `push` to `main` and `workflow_dispatch` (manual republish).
- **Permissions:** `contents: read`, `pages: write`, `id-token: write`. These are the minimum the
  Pages actions need.
- **Concurrency:** group `pages`, with `cancel-in-progress: false`, so two quick pushes publish in
  order and a running deploy is never cut off.
- **`build` job** (Ubuntu, Python 3.13, pip cache):
  1. `pip install -r requirements.txt`
  2. `python scripts/check_code.py`
  3. `python scripts/package.py`: the strict build, the internet check and the ZIP, in one step
  4. `python scripts/check_diagrams.py` with `EDGE` pointing at the runner's Google Chrome
  5. upload `site/` as the Pages artifact
- **`deploy` job:** needs `build`, and runs `actions/deploy-pages` in the `github-pages` environment.

Because `deploy` only runs after `build` succeeds, a failed check leaves the live site unchanged
(spec: *Checks guard the live site*).

*Python version:* 3.13 instead of the authors' 3.14, because the setup action and the pinned
packages are proven on it. Student code uses only the standard library, so the version does not
change behaviour. *Alternative:* 3.14, to match exactly. That is fine too once it is stable on
runners; it is a one-line change.

*Why `package.py` instead of a bare `mkdocs build`:* it adds the "nothing loads from the internet"
check for free. That check backs the spec scenario *Hosted site loads nothing from other sites*. The
ZIP it makes on the runner is thrown away.

### D3. Keep the `offline` plugin on for the hosted site

One configuration serves both outputs (spec: *Same content online and offline*). Over https, search
and every page work with the plugin on. *Alternative:* turn it off for the hosted build with an
environment variable. Rejected: two builds can drift apart, and the plugin costs nothing online.

### D4. Set `site_url`, and teach the internet check about it

`site_url: https://mohammusal.github.io/Cisco-Technology-Experience/` gives correct canonical links
and a `sitemap.xml`. Material then adds `<link rel="canonical" href="https://mohammusal.github.io/...">`
to every page. `package.py` treats any `<link href="https://...">` as a download, so the internet
check would fail.

Fix: make the check skip `<link rel="canonical">` (and `rel="alternate"` if present), because
browsers never download those. *Alternative:* add the Pages address to `ALLOWED`. Rejected: that
would also allow a real script or stylesheet loaded from that address, which would break the ZIP
offline.

### D5. Licence notices live next to the bundled files, inside `docs/`

- `docs/assets/fonts/OFL.txt`: the SIL Open Font License 1.1 text with the IBM Plex copyright line.
- `docs/assets/javascripts/THIRD-PARTY-NOTICES.txt`: Mermaid 11.17.2 (MIT) and iframe-worker
  1.0.4 (MIT), each with its copyright line and licence text.

Inside `docs/`, MkDocs copies them into `site/`, so the notices travel with the files on Pages and in
the ZIP, as the OFL asks. `.txt` files, not `.md`: they become static files, not pages that would
need a place in the navigation.

### D6. What goes into the repository

Everything that is not ignored: `docs/`, `code/`, `hooks/`, `scripts/`, `openspec/`, `mkdocs.yml`,
`requirements.txt`, `README.md`, `.gitignore`, and the new `.github/` and `.gitattributes`.

- **`.gitignore` additions:** the files the labs write (`notes.txt`, `temperatures.txt` under
  `code/`) and `.cache/`.
- **`.gitattributes`** with `* text=auto`, plus `*.png`, `*.woff2` and `*.zip` marked binary. This
  keeps line endings stable between Windows authors and the Linux runner.
- **`openspec/` is included.** It is the project's planning record. The older change still mentions
  Day 2 and timings. Bringing it up to date is separate work and does not block hosting.

### D7. First push and authentication

The first push is made from the authors' laptop, with `git init -b main`, the remote, a commit and
`git push -u origin main`. GitHub credentials come from the author's own Git Credential Manager. The
agent does not handle tokens.

Before pushing, `git ls-remote origin` shows whether the repository already has commits, for example
a README created on GitHub. If it does, fetch and rebase onto it instead of force-pushing.

## Risks / Trade-offs

- **[Risk]** Cisco branding (logo, name) is published on a personal GitHub account. → **Mitigation:**
  the owner confirms with the event organisers before the first push. Nothing in the build depends on
  the account, so the repository can later move to an organisation. The address then changes, which
  only matters for links already shared.
- **[Risk]** Everything in the repository is public, including `code/solutions/` and the
  instructor notes. → **Mitigation:** attendees already get both in the ZIP. Nothing secret is in
  the project.
- **[Risk]** The first Pages deploy can take several minutes, and the environment needs approving
  once. → **Mitigation:** publish well before the event and open the link on a phone to check it.
- **[Risk]** Chrome on the runner behaves differently from Edge for `check_diagrams.py`. →
  **Mitigation:** both use Chromium and the script only uses common headless flags. If the step is
  flaky, it can be marked `continue-on-error` without affecting publishing safety, because the strict
  build still guards the site.
- **[Trade-off]** The `pages` concurrency group publishes pushes one after another rather than
  skipping to the newest. This is slower with many quick pushes, but never leaves a half-published site.

## Migration Plan

1. Owner: confirm the branding is OK, then set **Settings > Pages > Source: GitHub Actions**.
2. Add the workflow, `site_url`, the internet-check fix, the licence notices, `.gitattributes` and
   the README section. Then run `check_code.py`, `package.py` and `check_diagrams.py` locally.
3. Initialise git, check the remote, commit and push to `main`.
4. Watch the workflow run in the **Actions** tab. Open the link in a desktop browser and on a phone.
5. Share the link with attendees, next to the ZIP.

**Rollback:** revert the bad commit and push, or re-run an earlier successful workflow run. To take
the site offline completely, unpublish it in **Settings > Pages**.
