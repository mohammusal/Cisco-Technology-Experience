# My Quiz Game
# This file grows a little at the end of every lab.

# --- Lab 1: say hello ---
name = input("What is your name? ")
print("Hello, " + name + "! Welcome to the Python Quiz.")

points = 0
print(f"{name}, you start with {points} points.")

# --- Lab 2: ask to start ---
start = input("Start the quiz? (Y/N) ")
if start == "Y" or start == "y":
    print("Great, let's go!")
else:
    print(f"No problem. See you next time, {name}!")
    exit()

# --- Lab 3: countdown, then ask until the answer is right ---
for number in range(3, 0, -1):
    print(number, "...")
print("Go!")

tries = 1
answer = input("What is the capital of Poland? ")
while answer != "Warsaw" and answer != "warsaw":
    print("Not quite. Try again!")
    answer = input("What is the capital of Poland? ")
    tries = tries + 1

print(f"Correct! You needed {tries} tries.")
points = points + 1
print(f"{name}, you have {points} points.")
