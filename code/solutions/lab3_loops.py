# Lab 3: Loops - solution

count = 5
while count > 0:
    print("Countdown:", count)
    count = count - 1
print("Lift off!")

table = 7
for i in range(1, 11):
    print(f"{i} x {table} = {i * table}")

for letter in "CISCO":
    print(letter)
for letter in "PYTHON":
    print(letter + " *")

for number in range(1, 11):
    if number == 4:
        continue
    if number == 8:
        break
    print("Number", number)

secret = 7
guess = int(input("Guess my number (1-10): "))
while guess != secret:
    print("Nope, try again!")
    guess = int(input("Guess my number (1-10): "))
print("You got it!")
