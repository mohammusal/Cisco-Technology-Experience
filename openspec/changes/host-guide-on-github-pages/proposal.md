# Proposal

## Why

Attendees should be able to open the lab guide from one shareable link, without first downloading
and unzipping anything. The guide already builds as a static MkDocs site, and the public repository
[mohammusal/Cisco-Technology-Experience](https://github.com/mohammusal/Cisco-Technology-Experience)
is ready to hold it, so GitHub Pages can serve it at no cost.

## What Changes

- Put the guide's source (`docs/`, `code/`, `hooks/`, `scripts/`, `mkdocs.yml`, `requirements.txt`,
  `README.md`, `openspec/`) under git and push it to the `main` branch of the repository. Build output
  (`site/`, `dist/`) and the local `.venv/` stay out of git.
- Add a GitHub Actions workflow. On every push to `main` it checks the student code, builds the
  site in strict mode, and publishes it to GitHub Pages. A failing check or build does not replace
  the live site.
- Set `site_url` in `mkdocs.yml` to the Pages address, so canonical links and the sitemap are correct.
- Keep the build identical for the hosted site and the offline ZIP. The ZIP keeps being shared with
  attendees through the group, as today. Nothing in it changes.
- Add licence notices for the third-party files bundled in the guide (IBM Plex fonts, Mermaid, the
  iframe-worker shim), because the repository is public.
- Document in `README.md` how publishing works, the one-time GitHub settings, and the shareable link.

Not in scope: a custom domain, a download button for the code on the site (the ZIP covers that),
changes to lab content, and a licence for the guide's own content (the organisers decide that).

## Capabilities

### New Capabilities
- `guide-hosting`: publishing the lab guide as a website from the GitHub repository. Covers the
  shareable address, automatic publishing with checks, keeping the hosted site and the ZIP the same,
  and what the public repository contains.

### Modified Capabilities
<!-- None. `lab-guide-site` exists only in the unarchived change `add-day1-python-lab-guide`, and its
     offline-handout requirements stay as they are. -->

## Impact

- **New files:** `.github/workflows/pages.yml`, licence notices next to the bundled fonts and scripts.
- **Changed files:** `mkdocs.yml` (`site_url`), `README.md` (publishing section), possibly `.gitignore`.
- **GitHub:** the repository gets its first push; Pages must be switched to "GitHub Actions" once in
  the repository settings by the owner.
- **Dependencies:** GitHub-hosted Ubuntu runner with Python; the pinned `requirements.txt` is reused.
- **Public visibility:** everything pushed is public, including `code/solutions/`, instructor notes in
  the pages, and the Cisco logo and name. Attendees already receive the solutions and notes in the ZIP.
