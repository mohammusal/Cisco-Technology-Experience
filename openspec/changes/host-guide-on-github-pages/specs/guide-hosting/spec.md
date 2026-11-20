# Spec Delta

## Purpose

Publishes the Python workshop lab guide as a public website from its GitHub repository, so attendees
can open it from one shareable link while the offline ZIP stays available.

## ADDED Requirements

### Requirement: Shareable link
The guide SHALL be available at one stable public address on GitHub Pages:
`https://mohammusal.github.io/Cisco-Technology-Experience/`. Opening that address SHALL show the
guide's home page without signing in.

#### Scenario: Attendee opens the link
- **WHEN** an attendee opens the shared link in a browser on a laptop or phone, without a GitHub account
- **THEN** the guide's home page loads with the same header, navigation and styling as the offline copy

#### Scenario: Deep link to a lab
- **WHEN** an instructor shares the address of a single page, for example Lab 3
- **THEN** that page opens directly, with working navigation, images and diagrams

### Requirement: Automatic publishing
Every push to the `main` branch SHALL rebuild and republish the site without manual steps on a laptop.

#### Scenario: Author pushes a fix
- **WHEN** an author pushes a corrected page to `main`
- **THEN** the hosted guide shows the correction within a few minutes, with no other action needed

#### Scenario: Manual republish
- **WHEN** the repository owner starts the publishing workflow by hand from GitHub
- **THEN** the site is rebuilt and republished from the current `main`

### Requirement: Checks guard the live site
Publishing SHALL run the student-code checks and a strict site build first. If either fails, the
site that is already live SHALL stay unchanged.

#### Scenario: Broken link in a page
- **WHEN** a push to `main` contains a page with a broken internal link
- **THEN** the strict build fails, the workflow is marked failed, and the live site still shows the previous version

#### Scenario: Broken starter code
- **WHEN** a push to `main` contains a starter or solution file that fails the code checks
- **THEN** nothing is published, and the failed check is visible on the commit in GitHub

### Requirement: Same content online and offline
The hosted site and the offline ZIP SHALL be built from the same source with the same configuration,
so a page shows the same content and works the same in both.

#### Scenario: Comparing a page
- **WHEN** an attendee opens Lab 4 from the link and a neighbour opens Lab 4 from the unzipped ZIP
- **THEN** both see the same text, code blocks, screenshots and diagrams

#### Scenario: Hosted site loads nothing from other sites
- **WHEN** the hosted guide is opened with the browser's network inspector
- **THEN** every font, script, stylesheet, image and diagram library is loaded from the guide's own address

### Requirement: Repository contents
The public repository SHALL contain the guide's source and student code, and SHALL NOT contain build
output, local virtual environments, or files the student programs write at run time.

#### Scenario: Fresh clone
- **WHEN** someone clones the repository
- **THEN** it has the pages, student code, build scripts and configuration needed to build the guide, and no `site/`, `dist/`, `.venv/` or `scores.txt`

### Requirement: Third-party notices
Every third-party file bundled in the guide SHALL have its licence notice in the repository.

#### Scenario: Checking a bundled font
- **WHEN** someone looks for the licence of the bundled IBM Plex fonts, Mermaid or the iframe-worker shim
- **THEN** a licence notice for each is in the repository next to the bundled files

### Requirement: Publishing instructions
The README SHALL explain the shareable link, the one-time GitHub settings, and how to publish and
check a change.

#### Scenario: New co-author publishes
- **WHEN** a co-author who has not published before reads the README
- **THEN** they can find the live link, enable Pages if needed, and know that pushing to `main` publishes
