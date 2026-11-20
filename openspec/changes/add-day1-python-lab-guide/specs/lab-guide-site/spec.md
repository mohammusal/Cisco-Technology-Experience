# Spec Delta

## Purpose

Provides the browsable lab guide for the Cisco Technology Experience Python workshop: a Cisco-styled site that instructors preview locally and students open offline from a handout ZIP.

## ADDED Requirements

### Requirement: Cisco visual identity
The site SHALL use Cisco styling: midnight navy as the primary colour, Cisco cyan as the accent, and the Cisco logo in the header and as the browser tab icon. It SHALL offer a light and a dark colour scheme.

#### Scenario: Header shows Cisco branding
- **WHEN** a student opens any page of the guide
- **THEN** the header shows the Cisco logo and the site title "Cisco Technology Experience - Python Workshop"
- **AND** the browser tab shows the Cisco icon

#### Scenario: Student switches to dark mode
- **WHEN** a student selects the dark mode toggle
- **THEN** every page switches to the dark scheme and keeps the navy and cyan identity

### Requirement: Code-themed landing page
The home page SHALL present the workshop as a code editor window echoing the slides, showing the workshop title, Kraków and the year. It SHALL link to the pre-work page, Lab 0 and the cheat sheet.

#### Scenario: Student lands on the home page
- **WHEN** a student opens the guide's start page
- **THEN** they see an editor-style window with workshop code text such as `class BeginnerLevelPythonProgramming:`
- **AND** they see entry links to "Before you come", "Lab 0" and "Cheat sheet"

#### Scenario: Animation does not block reading
- **WHEN** the student's browser has reduced motion enabled
- **THEN** the landing page shows the code text without animation

### Requirement: Day-based navigation
The site SHALL have top-level tabs for Home, Day 1, Day 2 and Help. The Day 2 tab SHALL be a placeholder page stating that Day 2 content will follow.

#### Scenario: Day 1 pages are in teaching order
- **WHEN** a student opens the Day 1 tab
- **THEN** the side navigation lists Before you come, Lab 0 to Lab 7 in order with the two break pages between them, and the cheat sheet

#### Scenario: Day 2 placeholder
- **WHEN** a student opens the Day 2 tab
- **THEN** a single page explains that Day 2 (APIs and Webex) will be added later

### Requirement: Lab progress map
Every lab page SHALL show a progress map of Lab 0 to Lab 7 at the top that marks completed labs, the current lab and upcoming labs.

#### Scenario: Student is on Lab 3
- **WHEN** a student opens Lab 3
- **THEN** the map shows Labs 0-2 as done, Lab 3 as current and Labs 4-7 as upcoming
- **AND** each lab in the map links to that lab's page

### Requirement: Beginner callout types
The site SHALL provide distinct, consistently styled callouts for Predict, Checkpoint, Error decoder, Pro tip, Analogy and Badge earned. Each callout type SHALL have its own icon and colour.

#### Scenario: Predict callout hides the answer
- **WHEN** a page shows a Predict callout
- **THEN** the expected output is hidden in a collapsed block that the student opens after guessing

#### Scenario: Callouts look the same everywhere
- **WHEN** the same callout type appears on two different lab pages
- **THEN** it has the same icon, colour and title style on both

### Requirement: Copyable code blocks
Every code block that students need to type or run SHALL have a copy button and syntax highlighting. Expected-output blocks SHALL be visually distinct from code to type.

#### Scenario: Student copies a code block
- **WHEN** a student clicks the copy button on a code block
- **THEN** the block's code is on the clipboard without line numbers or prompts

### Requirement: Glossary tooltips
Programming terms defined in the glossary SHALL show their plain-English definition when a student hovers over or taps them on any page.

#### Scenario: Hovering a term
- **WHEN** a student hovers over the word "variable" on a lab page
- **THEN** a tooltip shows its short definition from the glossary

### Requirement: Offline handout
The built site SHALL work fully when opened from the local file system with no network. That includes navigation between pages, search, images, icons and fonts.

#### Scenario: Opened from an unzipped folder without Wi-Fi
- **WHEN** a student unzips the handout, disconnects from the network and opens the start page
- **THEN** every page, image and icon loads, and moving between pages works

#### Scenario: Search works offline
- **WHEN** a student searches for "loop" in the offline handout
- **THEN** search returns matching pages

#### Scenario: No external requests
- **WHEN** the built site is inspected for external URLs that load fonts, scripts, stylesheets or images
- **THEN** none are found

### Requirement: Handout package
The project SHALL produce one ZIP file containing the built guide, the student code folder and a clearly named start file at the top level of the ZIP.

#### Scenario: Student finds where to start
- **WHEN** a student opens the unzipped handout folder
- **THEN** a `START_HERE.html` file at the top level opens the guide's home page
- **AND** a `code` folder holds the lab starter files and solutions

### Requirement: Local preview for authors
Authors SHALL be able to preview the guide with live reload on their own machine using one documented command, after a one-time documented install of pinned tool versions.

#### Scenario: Author previews changes
- **WHEN** an author runs the documented preview command and edits a page
- **THEN** the browser preview updates to show the edit

### Requirement: Readable beside VS Code
Lab pages SHALL stay readable when the browser takes up half of a laptop screen next to VS Code. That means no horizontal scrolling for normal text, and cards and grids stacking into one column.

#### Scenario: Half-screen browser
- **WHEN** a student views a lab page in a browser window about 700 pixels wide
- **THEN** text, callouts and concept cards fit the width without horizontal scrolling
