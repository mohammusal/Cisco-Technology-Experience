# Spec Delta

## Purpose

Defines the Day 1 learning content that turns slides 1-144 of the Python workshop deck into a mostly hands-on day that high school students with no programming experience can follow on their own.

## ADDED Requirements

### Requirement: Day 1 schedule
The guide SHALL publish a Day 1 schedule that alternates slide blocks with labs. It SHALL name each block's slide range and give planned minutes, totalling about 60 minutes of slides and 300 minutes of labs, with breaks listed separately.

#### Scenario: Instructor checks the timing
- **WHEN** an instructor opens the Day 1 schedule
- **THEN** each row shows a slide range (for example "Slides 20-28"), the lab that follows it and the minutes for both
- **AND** slide minutes add up to about 60 and lab minutes to about 300

#### Scenario: Slide ranges cover the deck
- **WHEN** the schedule's slide ranges are combined
- **THEN** they cover slides 1 to 144 in order without gaps or overlaps

### Requirement: Lab sequence and topics
Day 1 SHALL contain eight labs in this order, each mapped to its slide block:
- Lab 0 Setup
- Lab 1 Variables, types and operators
- Lab 2 Decisions
- Lab 3 Loops
- Lab 4 Lists and strings
- Lab 5 Tuple, dictionary and set
- Lab 6 Functions, files and exceptions
- Lab 7 Quiz Game project

#### Scenario: Lab follows its slides
- **WHEN** a student finishes the slide block on conditionals (slides 29-41)
- **THEN** the next lab in the guide is Lab 2 Decisions, which practises `if`, `elif`, `else`, comparisons and indentation

### Requirement: Lab page structure
Every lab page SHALL open with its duration, what students will build, the matching slide numbers and an analogy card for each concept. It SHALL then give numbered steps and end with that lab's Quiz Game step and a Badge earned callout.

#### Scenario: Student opens a lab
- **WHEN** a student opens Lab 3 Loops
- **THEN** the top of the page shows the time (for example "35 min"), the related slides and analogy cards such as "a loop is a playlist on repeat"
- **AND** the last section adds the Lab 3 piece to the Quiz Game and awards a badge

### Requirement: Beginner-sized steps
Each step SHALL introduce at most one new concept and ask the student to type or change no more than about five lines of code before running it. Every run SHALL show its expected output.

#### Scenario: Step with a run
- **WHEN** a step asks the student to run their file
- **THEN** the step shows the exact command or button to use and the exact output the student should see

### Requirement: Plain-language explanations
Explanations SHALL use plain English suitable for high school students who are not native English speakers. They SHALL use short sentences, define every programming term on first use, and avoid jargon that the slides have not introduced.

#### Scenario: New term appears
- **WHEN** a lab page uses the word "index" for the first time
- **THEN** the sentence explains it, or the word links to its glossary definition

### Requirement: Predict before running
Each lab SHALL include at least two Predict callouts, where the student guesses the output of a short snippet before running it and then reveals the answer.

#### Scenario: Predict exercise
- **WHEN** a student reaches a Predict callout in Lab 4
- **THEN** they see a snippet such as `cisco[-1]`, are asked what it prints, and can reveal `'o'` with a one-line explanation

### Requirement: Error decoders
Each lab SHALL include Error decoder callouts for the errors beginners most often hit with that lab's concepts. Each decoder SHALL show the real error message, say what it means in plain English and give the fix.

#### Scenario: Missing colon
- **WHEN** a student's `if` line has no colon and Python reports `SyntaxError: expected ':'`
- **THEN** the Lab 2 error decoder for that message explains that every `if`, `elif`, `else`, `for`, `while` and `def` line ends with a colon, and shows the fixed line

#### Scenario: Errors covered across the day
- **WHEN** all labs' error decoders are combined
- **THEN** they cover at least `SyntaxError`, `IndentationError`, `NameError`, `TypeError`, `ValueError`, `IndexError`, `KeyError` and `ZeroDivisionError`

### Requirement: Three difficulty levels
Each lab's practice exercises SHALL offer three tabs:
- **Follow along:** the full code is given.
- **Try it:** hints are given but not the full code.
- **Challenge:** a stretch task with no code given.

A student SHALL be able to complete the lab's Quiz Game step using Follow along alone.

#### Scenario: Fast student
- **WHEN** a student finishes an exercise early
- **THEN** the Challenge tab gives them an extra task on the same concept

#### Scenario: Struggling student
- **WHEN** a student cannot solve an exercise from the hints
- **THEN** the Follow along tab gives the complete code and its expected output

### Requirement: Checkpoints
Each lab SHALL end with a Checkpoint callout listing what the student's program prints and which solution file to load if theirs does not match.

#### Scenario: Student falls behind
- **WHEN** a student's program does not match the Lab 5 checkpoint
- **THEN** the checkpoint names the Lab 5 solution file to copy so they can start Lab 6 from a working version

### Requirement: Pre-work and Lab 0 setup
A "Before you come" page SHALL guide students to install Python 3 and VS Code with the Python extension and run a hello-world file. It SHALL have separate tabs for Windows and macOS with a screenshot for each key screen. Lab 0 SHALL be a short on-the-day check of the same result.

#### Scenario: Windows install
- **WHEN** a Windows student follows the Windows tab
- **THEN** the guide explicitly shows ticking "Add python.exe to PATH" in the installer and how to check the install in a terminal

#### Scenario: macOS command name
- **WHEN** a macOS student follows the macOS tab
- **THEN** the guide uses `python3` in every command

#### Scenario: Lab 0 check
- **WHEN** a student who did the pre-work starts Lab 0
- **THEN** they can confirm their setup in under 15 minutes by running `hello.py` and seeing `Hello World` (slide 18)

### Requirement: VS Code only
All Day 1 coding SHALL happen in VS Code with a local Python install. The guide SHALL NOT direct students to a browser-based Python editor. For a laptop that cannot run Python, it SHALL tell the student to pair with a neighbour and ask an instructor.

#### Scenario: Laptop cannot run Python
- **WHEN** a student's laptop still cannot run Python after the troubleshooting steps
- **THEN** the troubleshooting page tells them to pair with a neighbour on that laptop and call an instructor

### Requirement: Troubleshooting page
The Help tab SHALL have a troubleshooting page covering the setup and run problems expected on student laptops, each with symptoms and a fix.

#### Scenario: Python opens the Microsoft Store
- **WHEN** typing `python` on Windows opens the Microsoft Store
- **THEN** the troubleshooting page explains the app execution alias and how to fix it or use `py`

#### Scenario: VS Code uses the wrong Python
- **WHEN** VS Code runs the file with a different or missing interpreter
- **THEN** the troubleshooting page shows how to choose the interpreter from the status bar

### Requirement: Break pages
The Day 1 navigation SHALL include break pages at the points the slides schedule them: after the first slide block (10 minutes) and before Functions (15 minutes).

#### Scenario: Student reaches a break
- **WHEN** a student finishes the lab before a break
- **THEN** the next page is a break page that tells them to stop, rest and wait for the instructor before continuing

### Requirement: Accurate Python facts
The labs SHALL teach behaviour that matches current Python 3, even where the slides are imprecise.

#### Scenario: Dictionary order
- **WHEN** Lab 5 explains dictionaries
- **THEN** it states that dictionaries keep the order in which items were added, and that keys cannot be lists while values can be any type

### Requirement: Cheat sheet
Day 1 SHALL include a one-page cheat sheet summarising every concept from Labs 1-6 with one tiny example each. It SHALL fit on a single printed A4 page.

#### Scenario: Printing the cheat sheet
- **WHEN** a student prints the cheat sheet page from the browser
- **THEN** it prints on one A4 page without navigation menus

### Requirement: Glossary
The guide SHALL include a glossary of every programming term used on Day 1, each with a definition of one or two sentences written for beginners.

#### Scenario: Looking up a term
- **WHEN** a student opens the glossary
- **THEN** terms such as variable, string, list, index, loop, function and exception each have a short beginner-level definition
