# Spec Delta

## Purpose

Provides the Python files students open in VS Code on Day 1: practice starters for each lab and a Quiz Game that grows one step per lab, with solutions that let anyone who falls behind catch up.

## ADDED Requirements

### Requirement: Code folder layout
The student code folder SHALL contain:
- one folder per lab (Lab 0 to Lab 7) holding that lab's practice starter files
- a `quiz.py` working file
- a question bank file
- a solutions folder

#### Scenario: Student opens the code folder in VS Code
- **WHEN** a student opens the `code` folder in VS Code
- **THEN** they see `lab0` to `lab7` folders, `quiz.py`, `questions.py` and `solutions`, with names that match the lab guide

### Requirement: Runs with standard Python only
All student code and solutions SHALL run on Python 3.10 or newer on Windows and macOS. They SHALL use only the standard library and need no extra install.

#### Scenario: Fresh Python install
- **WHEN** a student with a fresh Python 3 install and no extra packages runs any solution file
- **THEN** it runs without import errors

### Requirement: Starter files with marked gaps
Each practice starter file SHALL run without errors as given. It SHALL mark every place the student edits with a numbered `TODO` comment that matches the step number in the guide.

#### Scenario: Matching a TODO to the guide
- **WHEN** Lab 2 step 3 tells the student to complete `TODO 3`
- **THEN** the Lab 2 starter file contains a comment `# TODO 3` at the place to edit

### Requirement: Quiz Game grows one step per lab
The Quiz Game SHALL gain one feature at the end of each of Labs 1-6 and be completed in Lab 7, so that the game after each lab behaves as described in the scenarios below.

#### Scenario: Game after Lab 1
- **WHEN** a student runs the Lab 1 version and types their name
- **THEN** the program greets them by that name

#### Scenario: Game after Lab 2
- **WHEN** a student runs the Lab 2 version and answers `n` to "Start the quiz? (Y/N)"
- **THEN** the program prints a goodbye message and ends without asking questions

#### Scenario: Game after Lab 3
- **WHEN** a student runs the Lab 3 version and gives a wrong answer
- **THEN** the game asks the same question again until the answer is correct

#### Scenario: Game after Lab 4
- **WHEN** the game picks a question at random, the correct answer is `warsaw` and the student types `  Warsaw `
- **THEN** the game counts the answer as correct

#### Scenario: Game after Lab 5
- **WHEN** a student runs the Lab 5 version
- **THEN** the questions come from the question bank and the game shows the player's score

#### Scenario: Game after Lab 6
- **WHEN** a student runs the Lab 6 version
- **THEN** each question is asked through a function, bad input is handled, and the score is saved to a file

#### Scenario: Game after Lab 7
- **WHEN** a student runs the Lab 7 version
- **THEN** the game plays 5 rounds with the 30-second rule and shows the top scores

### Requirement: Catch-up solution after each lab
The solutions folder SHALL contain a working Quiz Game file for the end of every lab, from Lab 1 to Lab 7, and solutions for each lab's practice exercises. Each Quiz Game solution SHALL be a valid starting point for the next lab.

#### Scenario: Student catches up
- **WHEN** a student copies the Lab 4 Quiz Game solution over their `quiz.py`
- **THEN** they can follow Lab 5 step by step and get the outputs the guide shows

### Requirement: Final Quiz Game behaviour
The final Quiz Game SHALL do everything slide 144 asks:
- greet the player by name
- confirm the start (Y/N)
- ask 5 randomly selected questions with no repeats in a round
- add a point for each correct answer and take one away for each wrong answer
- show the final score

#### Scenario: Full round
- **WHEN** a player enters their name, answers `Y` and answers 5 questions, 3 right and 2 wrong within the time limit
- **THEN** each answer gets immediate right or wrong feedback, and the game shows a final score of 1

#### Scenario: No repeated questions
- **WHEN** a player plays one round
- **THEN** none of the 5 questions appears twice

### Requirement: 30-second answer rule
For each question the final game SHALL measure the time from asking to answering. An answer given after more than 30 seconds SHALL score zero points, whether it is right or wrong, and the game SHALL say it was too slow.

#### Scenario: Slow answer
- **WHEN** a player answers correctly after 35 seconds
- **THEN** the game tells them they took too long and adds no points

#### Scenario: Fast answer
- **WHEN** a player answers correctly after 10 seconds
- **THEN** the game adds one point

### Requirement: Invalid input does not crash the game
The game from Lab 6 onward SHALL handle unexpected input without stopping with an error. Examples are an empty name or an unexpected reply to the Y/N prompt.

#### Scenario: Unexpected start reply
- **WHEN** the player types `maybe` at the "Start the quiz? (Y/N)" prompt
- **THEN** the game asks again instead of crashing or starting

### Requirement: Score saved to a file
From Lab 6 onward the game SHALL append the player's name and final score to a scores file next to the game. From Lab 7 it SHALL show the top 3 scores at the end of each game. A missing scores file SHALL NOT cause an error.

#### Scenario: First game ever
- **WHEN** no scores file exists and a player finishes a game
- **THEN** the game creates the file with that player's name and score and shows them as the only top score

#### Scenario: Several players
- **WHEN** five players have finished games
- **THEN** the end screen lists the three highest scores with names, highest first

### Requirement: Question bank
The question bank SHALL be a separate, plain Python file holding at least 15 short questions. Each question SHALL have a one-word or one-number answer, and together they SHALL cover Kraków and Poland, technology and Cisco, the day's Python, and general fun. Adding a question SHALL require editing only this file.

#### Scenario: Instructor adds a question
- **WHEN** an instructor adds a new question and answer to the question bank and saves it
- **THEN** the next game can pick that question without any change to `quiz.py`

#### Scenario: Answers are simple
- **WHEN** any question in the bank is asked
- **THEN** its correct answer is a single word or number that a beginner can type
