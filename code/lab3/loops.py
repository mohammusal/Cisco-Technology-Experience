# Lab 3: Loops
# Run this file after each TODO. It works even before you change anything.

# TODO 1: A while loop repeats while the condition is True.
count = 5
while count > 0:
    print("Countdown:", count)
    count = count - 1
print("Lift off!")

# TODO 2: range() makes numbers for a for loop. Change 7 to any number.
table = 7
for i in range(1, 11):
    print(f"{i} x {table} = {i * table}")

# TODO 3: A for loop can walk through the letters of a string.
for letter in "CISCO":
    print(letter)
# Now remove the # below and make each letter appear with a star after it.
# for letter in "PYTHON":
#     print(letter + " *")

# TODO 4: break stops a loop. continue skips to the next round.
for number in range(1, 11):
    if number == 4:
        continue  # skip 4
    if number == 8:
        break  # stop at 8
    print("Number", number)

# TODO 5: Guess the secret number. Remove the # in front of the 6 lines below.
# secret = 7
# guess = int(input("Guess my number (1-10): "))
# while guess != secret:
#     print("Nope, try again!")
#     guess = int(input("Guess my number (1-10): "))
# print("You got it!")
