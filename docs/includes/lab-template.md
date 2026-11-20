---
lab: 1                 # 0-7: drives the progress map (done / current / upcoming)
file: 01-variables.py  # the "file tab" shown above the title, like a VS Code tab
---

<!--
LAB PAGE TEMPLATE
=================
Copy this file to docs/day1/labN-topic.md and add it to the nav in mkdocs.yml.
This folder (docs/includes/) is excluded from the build, so this file never becomes a page.

Rules for every lab:
- Write for someone who has never programmed: short sentences, one idea per sentence.
- Define every new word on first use, or add it to docs/includes/abbreviations.md (glossary + tooltip).
- Every code block must run as shown. Copy expected output from a real run.
- Step N.M matches "# TODO M" in code/labN/<file>.py.
- Solutions live in code/solutions/ and are included with snippets, never pasted twice.
- Run `python scripts/check_code.py` and `mkdocs build --strict` before you commit.
-->

# Lab N - Topic in plain words

<!-- The summary strip: slides, what the student builds, which file. -->
<div class="lab-summary" markdown>
**:material-presentation: After slides X-Y** <span class="slides-chip">Slide section title</span>

**:material-hammer-wrench: You build:** one sentence a student is proud of

**:material-file-code: File:** `labN/file.py`
</div>

One or two sentences: why this matters, linked to the Quiz Game.

<!-- Concept cards: 2-4 cards, each with a title, one sentence and a real-life comparison. -->
<div class="concepts" markdown>
<div markdown>
<p class="card-title">Concept</p>
One sentence that defines it, with a tiny `code` example.
<p class="like">an everyday comparison</p>
</div>
<div markdown>
<p class="card-title">Second concept</p>
One sentence.
<p class="like">an everyday comparison</p>
</div>
</div>

## Steps

Open `labN/file.py`. For each step, find its `TODO`.

### <span class="step-num">N.1</span> Short step title

Find `TODO 1` and run. (Say exactly which `#` to remove.)

```python title="labN/file.py"
print("code exactly as in the starter file")
```

<!-- Expected output: always a text block titled Output (styled green). -->
```text title="Output"
code exactly as in the starter file
```

<!-- Predict: make them think BEFORE they run. The answer stays hidden. -->
!!! predict "Predict"
    What does this print?

    ```python
    print(2 + 3)
    ```

    ??? success "Show the answer"
        `5`, and one sentence explaining why.

<!-- Error decoder: the exact error text in the title, then what it means and how to fix it. -->
!!! error "Error decoder: `NameError: name 'x' is not defined`"
    **What it means:** plain words.

    **How to fix it:** concrete steps.

<!-- Analogy: for the one idea in the lab that is hardest to picture. -->
!!! analogy "Think of it like..."
    A comparison from everyday life.

<!-- VS Code tip: a shortcut or a VS Code feature that helps right now. -->
!!! vscode "VS Code tip"
    Press ++ctrl+slash++ to comment a line in or out.

## Practise: exercise title

<!-- Three tabs: copy the code / write it with hints / stretch goals. -->
=== "Follow along"

    Create `labN/exercise.py` and type:

    ```python title="labN/exercise.py"
    --8<-- "code/solutions/lab1_exercise.py"
    ```

=== "Try it"

    The task in one or two sentences.

    **Hints:** the functions or ideas to use.

=== "Challenge"

    - A harder variation.
    - Another one.

## Add it to your Quiz Game

What to add to `quiz.py`, where to add it, and the full code block for the new part.

```text title="Output"
what the game shows now
```

!!! checkpoint "Checkpoint"
    One sentence: what the game can do now.

    Not the same? Copy `code/solutions/quiz_after_labN.py` over your `quiz.py`.

!!! badge "Badge earned"
    **Badge Name**

    One sentence about what they can do now.

<!-- Instructor notes: collapsed, so students skip them. -->
??? instructor "For instructors"
    - Common student questions, and which slides the exercise matches.
