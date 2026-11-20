# Lab 1: Variables, types and operators
# Run this file after each TODO. It works even before you change anything.

# TODO 1: Change the values so they describe YOU.
name = "Your name"
age = 15
city = "Krakow"
print(name)
print(age)
print(city)

# TODO 2: Remove the # in front of each line to see the type of each value.
# print(type(name))
# print(type(age))
# print(type(1.75))
# print(type(True))

# TODO 3: Pocket money calculator. Change the numbers, then run.
pocket_money = 50      # zloty per week
weeks = 4
total = pocket_money * weeks
print("In", weeks, "weeks I get", total, "zloty")
# Try the other operators too. Remove the # first.
# print(17 / 5)    # divide
# print(17 // 5)   # divide and drop the rest
# print(17 % 5)    # only the rest
# print(2 ** 10)   # power: 2 x 2 x 2 ... ten times

# TODO 4: Join text. Line A works. Line B breaks. Line C fixes it.
print("Hello, " + name + "!")                 # A
# print("I am " + age + " years old")        # B: remove the # and run. What happens?
# print(f"I am {age} years old")             # C: an f-string puts values inside text

# TODO 5: Ask the user. input() always gives you a string.
# year = input("Which year were you born? ")
# age_next_year = 2027 - int(year)
# print(f"In 2027 you will be {age_next_year}.")
