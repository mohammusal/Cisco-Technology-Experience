"""Check the student code: every starter runs, and every solution behaves as the guide says.

Run from the project root:   python scripts/check_code.py

Each file runs in a fresh temporary folder (so scores.txt starts empty), with
scripted answers for input() and a fake clock for the 30-second rule.
"""

import builtins
import contextlib
import io
import os
import runpy
import shutil
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CODE = ROOT / "code"
SOLUTIONS = CODE / "solutions"

sys.path.insert(0, str(CODE))
from questions import QUESTIONS  # noqa: E402

LAB4_QUESTIONS = {
    "What is the capital of Poland?": "warsaw",
    "Which river flows through Krakow?": "vistula",
    "How many legs does a spider have?": "8",
}

failures = []
temp_folders = []


class Clock:
    def __init__(self):
        self.now = 1_000_000.0

    def time(self):
        return self.now


class Player:
    """Answers input() prompts. Quiz questions are answered from a plan."""

    def __init__(self, clock, replies=None, plan=None, bank=None):
        self.clock = clock
        self.replies = {key: list(value) if isinstance(value, list) else [value]
                        for key, value in (replies or {}).items()}
        self.plan = list(plan or [])
        self.bank = bank or {}
        self.prompts = []

    def __call__(self, prompt=""):
        self.prompts.append(prompt)
        print(prompt, end="")
        question = prompt.strip()
        if question in self.bank:
            kind = self.plan.pop(0) if self.plan else "right"
            correct = self.bank[question]
            if kind == "slow":
                self.clock.now += 35
                return correct
            self.clock.now += 5
            return f"  {correct.upper()} " if kind == "right" else "nope"
        for key, values in self.replies.items():
            if key in prompt:
                return values.pop(0) if len(values) > 1 else values[0]
        return ""


def run(path, replies=None, plan=None, bank=None, files=None, questions=None):
    """Run one file and return (output, folder it ran in)."""
    folder = Path(tempfile.mkdtemp(prefix="quizcheck_"))
    temp_folders.append(folder)
    (folder / "questions.py").write_text(
        questions if questions is not None else (CODE / "questions.py").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    for name, text in (files or {}).items():
        (folder / name).write_text(text, encoding="utf-8")

    clock = Clock()
    player = Player(clock, replies, plan, bank)
    out = io.StringIO()
    old_cwd, old_input, old_time = Path.cwd(), builtins.input, time.time
    sys.modules.pop("questions", None)
    sys.path.insert(0, str(folder))
    try:
        os.chdir(folder)
        builtins.input = player
        time.time = clock.time
        with contextlib.redirect_stdout(out):
            try:
                runpy.run_path(str(path), run_name="__main__")
            except SystemExit:
                pass
    finally:
        builtins.input, time.time = old_input, old_time
        os.chdir(old_cwd)
        sys.path.remove(str(folder))
        sys.modules.pop("questions", None)
    return out.getvalue(), folder


def expect(label, output, *needles, absent=()):
    missing = [n for n in needles if n not in output]
    present = [n for n in absent if n in output]
    if missing or present:
        failures.append(label)
        print(f"FAIL  {label}")
        for n in missing:
            print(f"      missing: {n!r}")
        for n in present:
            print(f"      should not appear: {n!r}")
    else:
        print(f"ok    {label}")


def check_starters():
    starters = sorted(CODE.glob("lab*/*.py")) + [CODE / "quiz.py"]
    for path in starters:
        label = f"starter runs: {path.relative_to(CODE).as_posix()}"
        try:
            run(path)
        except Exception as error:  # noqa: BLE001 - any crash is a failure
            failures.append(label)
            print(f"FAIL  {label} -> {error!r}")
            continue
        if path.name != "quiz.py" and "# TODO " not in path.read_text(encoding="utf-8"):
            failures.append(label)
            print(f"FAIL  {label}: no numbered TODO markers")
            continue
        print(f"ok    {label}")


PRACTICE_REPLIES = {
    "born": "2010",
    "How many people": "10",
    "slices": "3",
    "How old": "15",
    "Which day": "Saturday",
    "Guess my number": ["3", "7"],
    "First name": "Ola",
    "Last name": "Nowak",
    "Year you were born": "2010",
    "Polish word": "smok",
}

PRACTICE_EXPECT = {
    "lab0_hello.py": ["Hello World", "Python says hi!"],
    "lab0_exercise.py": ["OLA NOWAK"],
    "lab1_variables.py": ["<class 'int'>", "In 4 weeks I get 200 zloty", "1024", "In 2027 you will be 17."],
    "lab1_exercise.py": ["You need 30 slices.", "Order 4 pizzas.", "159.6 zloty"],
    "lab2_decisions.py": ["You can watch the film.", "gives grade 4", "Have fun!"],
    "lab2_exercise.py": ["Your ticket costs 20 zloty."],
    "lab3_loops.py": ["Lift off!", "10 x 7 = 70", "N *", "Number 7", "You got it!"],
    "lab3_exercise.py": ["= 5050", "FizzBuzz"],
    "lab4_lists_and_strings.py": ["['s', 'c', 'o']", "#4 : o", "WE ARE CISCO", "We *** are *** Cisco"],
    "lab4_exercise.py": ["Your username is: olanow10", "Vowels in your name: 4"],
    "lab5_collections_practice.py": ["('Ola', 7)", "A spider has 8 legs", "3 different visitors"],
    "lab5_exercise.py": ["smok -> dragon", "'k': 2"],
    "lab6_functions.py": ["1.4", "25", "Next year you will be 16.", "Read: Python is fun", "IndexError"],
    "lab6_exercise.py": ["30 C = 86.0 F, hot: True", "You cannot divide by zero!"],
    "lab7_timer_practice.py": ["Your reaction time:", "1. Jan - 5 points", "3. Ania - 3 points"],
}


def check_practice_solutions():
    for name, needles in PRACTICE_EXPECT.items():
        output, _ = run(SOLUTIONS / name, replies=PRACTICE_REPLIES)
        expect(f"practice solution: {name}", output, *needles)


def check_quiz():
    s = SOLUTIONS
    output, _ = run(s / "quiz_after_lab1.py", replies={"name": "Ada"})
    expect("lab1: greets by name", output, "Hello, Ada! Welcome", "Ada, you start with 0 points.")

    output, _ = run(s / "quiz_after_lab2.py", replies={"name": "Ada", "Start": "n"})
    expect("lab2: N ends politely", output, "See you next time, Ada!", absent=["capital"])
    output, _ = run(s / "quiz_after_lab2.py", replies={"name": "Ada", "Start": "y", "capital": "Warsaw"})
    expect("lab2: one question", output, "Correct! +1 point", "Ada, you have 1 points.")

    output, _ = run(s / "quiz_after_lab3.py",
                    replies={"name": "Ada", "Start": "Y", "capital": ["Krakow", "Warsaw"]})
    expect("lab3: asks until correct", output, "3 ...", "Go!", "Not quite", "You needed 2 tries.")

    output, _ = run(s / "quiz_after_lab4.py", replies={"name": "Ada", "Start": " Y "},
                    bank=LAB4_QUESTIONS, plan=["right"])
    expect("lab4: random pick, case and spaces ignored", output, "Correct! You needed 1 tries.")

    extra = 'QUESTIONS = {"A": "1", "B": "2", "Brand new question?": "new"}\n'
    output, _ = run(s / "quiz_after_lab5.py", replies={"name": "Ada", "Start": "y"},
                    bank={"A": "1", "B": "2", "Brand new question?": "new"},
                    plan=["right", "right", "wrong"], questions=extra)
    expect("lab5: question bank, +1/-1 score", output, "Brand new question?", "Wrong!", "your score is 1.")

    output, folder = run(s / "quiz_after_lab6.py",
                         replies={"name": ["", "Ada"], "Start": ["maybe", "y"]},
                         bank=QUESTIONS, plan=["right", "right", "right"])
    expect("lab6: re-asks name and Y/N", output, "Please type at least one letter.", "Please type Y or N.")
    saved = (folder / "scores.txt").read_text(encoding="utf-8") if (folder / "scores.txt").exists() else ""
    expect("lab6: creates scores.txt", saved, "Ada,3")
    expect("lab6: reads scores back", output, "Games played so far: 1")

    output, folder = run(s / "quiz_final.py", replies={"name": "Ada", "Start": "y"},
                         bank=QUESTIONS, plan=["right", "right", "right", "wrong", "wrong"])
    expect("final: 3 right, 2 wrong = 1", output, "Question 5 of 5", "final score is 1.",
           "=== TOP 3 ===", "1. Ada - 1 points")

    output, _ = run(s / "quiz_final.py", replies={"name": "Ada", "Start": "y"},
                    bank=QUESTIONS, plan=["slow", "right", "right", "right", "right"])
    expect("final: slow answer scores 0", output, "Too slow! You took 35 seconds. 0 points", "final score is 4.")

    output, _ = run(s / "quiz_final.py", replies={"name": "Ada", "Start": "y"},
                    bank=QUESTIONS, plan=["wrong"] * 5,
                    files={"scores.txt": "Ola,2\nJan,5\nKuba,-1\nZosia,4\n"})
    expect("final: top 3 highest first", output,
           "1. Jan - 5 points\n2. Zosia - 4 points\n3. Ola - 2 points")

    for _ in range(3):
        output, _ = run(s / "quiz_final.py", replies={"name": "Ada", "Start": "y"}, bank=QUESTIONS)
        questions = [q for q in QUESTIONS if q in output]
        if len(questions) != 5:
            failures.append("final: 5 different questions")
            print(f"FAIL  final: 5 different questions (got {len(questions)})")
            break
    else:
        print("ok    final: 5 different questions in a round")


def check_question_bank():
    expect("question bank has 15 or more questions", str(len(QUESTIONS) >= 15), "True")
    bad = [a for a in QUESTIONS.values() if a != a.lower() or " " in a or not a.isascii()]
    expect("answers are one lowercase ASCII word", ", ".join(bad) or "none", "none")
    same = (CODE / "questions.py").read_bytes() == (SOLUTIONS / "questions.py").read_bytes()
    expect("solutions/questions.py matches code/questions.py", str(same), "True")


if __name__ == "__main__":
    print(f"Python {sys.version.split()[0]}")
    check_question_bank()
    check_starters()
    check_practice_solutions()
    check_quiz()
    for folder in temp_folders:
        shutil.rmtree(folder, ignore_errors=True)
    print()
    if failures:
        print(f"{len(failures)} check(s) failed.")
        sys.exit(1)
    print("All checks passed.")
