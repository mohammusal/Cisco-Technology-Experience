# My Quiz Game - the finished version (Lab 7)

import random
import time
from questions import QUESTIONS

ROUNDS = 5
TIME_LIMIT = 30  # seconds per question


def ask_name():
    name = input("What is your name? ").strip().replace(",", "")
    while name == "":
        print("Please type at least one letter.")
        name = input("What is your name? ").strip().replace(",", "")
    return name


def ask_yes_no(prompt):
    while True:
        reply = input(prompt).strip().lower()
        if reply == "y" or reply == "yes":
            return True
        if reply == "n" or reply == "no":
            return False
        print("Please type Y or N.")


def ask_question(question, correct):
    start_time = time.time()
    answer = input(question + " ").strip().lower()
    seconds = round(time.time() - start_time)

    if seconds > TIME_LIMIT:
        print(f"Too slow! You took {seconds} seconds. 0 points")
        return 0
    if answer == correct:
        print(f"Correct! +1 point ({seconds} seconds)")
        return 1
    print(f"Wrong! The answer was {correct}. -1 point")
    return -1


def save_score(name, points):
    with open("scores.txt", "a") as file:
        file.write(f"{name},{points}\n")


def load_scores():
    scores = []
    try:
        with open("scores.txt") as file:
            for line in file:
                player, points = line.strip().split(",")
                scores.append((int(points), player))
    except FileNotFoundError:
        pass  # No games saved yet: start with an empty list.
    return scores


def show_top_scores():
    top = sorted(load_scores(), reverse=True)[:3]
    print("=== TOP 3 ===")
    place = 1
    for points, player in top:
        print(f"{place}. {player} - {points} points")
        place = place + 1


# --- The game ---
print("=" * 30)
print("   THE BIG PYTHON QUIZ")
print("=" * 30)

name = ask_name()
print("Hello, " + name + "! Welcome to the Python Quiz.")
print(f"You get {ROUNDS} questions and {TIME_LIMIT} seconds for each one.")

if not ask_yes_no("Start the quiz? (Y/N) "):
    print(f"No problem. See you next time, {name}!")
    exit()

for number in range(3, 0, -1):
    print(number, "...")
print("Go!")

points = 0
round_number = 1
for question in random.sample(list(QUESTIONS.keys()), ROUNDS):
    print(f"\nQuestion {round_number} of {ROUNDS}")
    points = points + ask_question(question, QUESTIONS[question])
    round_number = round_number + 1

print(f"\nWell played, {name}! Your final score is {points}.")
save_score(name, points)
show_top_scores()
