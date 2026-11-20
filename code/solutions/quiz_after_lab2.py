# My Quiz Game
# This file grows a little at the end of every lab.

# --- Lab 1: say hello ---
name = input("What is your name? ")
print("Hello, " + name + "! Welcome to the Python Quiz.")

points = 0
print(f"{name}, you start with {points} points.")

# --- Lab 2: ask to start, then ask one question ---
start = input("Start the quiz? (Y/N) ")
if start == "Y" or start == "y":
    print("Great, let's go!")
else:
    print(f"No problem. See you next time, {name}!")
    exit()

answer = input("What is the capital of Poland? ")
if answer == "Warsaw" or answer == "warsaw":
    print("Correct! +1 point")
    points = points + 1
else:
    print("Not this time. The answer is Warsaw.")

print(f"{name}, you have {points} points.")
