# My Quiz Game
# This file grows a little at the end of every lab.

import random

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

# --- Lab 4: pick a random question from two lists ---
questions = [
    "What is the capital of Poland?",
    "Which river flows through Krakow?",
    "How many legs does a spider have?",
]
answers = ["warsaw", "vistula", "8"]

number = random.randint(0, len(questions) - 1)
question = questions[number]
correct = answers[number]

tries = 1
answer = input(question + " ").strip().lower()
while answer != correct:
    print("Not quite. Try again!")
    answer = input(question + " ").strip().lower()
    tries = tries + 1

print(f"Correct! You needed {tries} tries.")
points = points + 1
print(f"{name}, you have {points} points.")
