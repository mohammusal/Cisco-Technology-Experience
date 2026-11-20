# My Quiz Game
# This file grows a little at the end of every lab.
# Lab 6: the same game, tidied into functions.

import random
from questions import QUESTIONS

ROUNDS = 3


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
    answer = input(question + " ").strip().lower()
    if answer == correct:
        print("Correct! +1 point")
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


# --- The game ---
name = ask_name()
print("Hello, " + name + "! Welcome to the Python Quiz.")

if not ask_yes_no("Start the quiz? (Y/N) "):
    print(f"No problem. See you next time, {name}!")
    exit()

for number in range(3, 0, -1):
    print(number, "...")
print("Go!")

points = 0
for question in random.sample(list(QUESTIONS.keys()), ROUNDS):
    points = points + ask_question(question, QUESTIONS[question])

print(f"{name}, your score is {points}.")
save_score(name, points)
print(f"Saved! Games played so far: {len(load_scores())}")
