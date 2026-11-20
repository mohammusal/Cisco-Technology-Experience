# My Quiz Game
# This file grows a little at the end of every lab.

import random
from questions import QUESTIONS

# --- Lab 1: say hello ---
name = input("What is your name? ")
print("Hello, " + name + "! Welcome to the Python Quiz.")

points = 0
print(f"{name}, you start with {points} points.")

# --- Lab 2: ask to start (Lab 4: any case, any spaces) ---
start = input("Start the quiz? (Y/N) ").strip().lower()
if start == "y":
    print("Great, let's go!")
else:
    print(f"No problem. See you next time, {name}!")
    exit()

# --- Lab 3: countdown ---
for number in range(3, 0, -1):
    print(number, "...")
print("Go!")

# --- Lab 5: 3 different questions from the question bank, +1 or -1 ---
chosen = random.sample(list(QUESTIONS.keys()), 3)

for question in chosen:
    correct = QUESTIONS[question]
    answer = input(question + " ").strip().lower()
    if answer == correct:
        print("Correct! +1 point")
        points = points + 1
    else:
        print(f"Wrong! The answer was {correct}. -1 point")
        points = points - 1

print(f"{name}, your score is {points}.")
