# Lab 2 exercise: cinema ticket machine - solution

age = int(input("How old are you? "))
day = input("Which day is it? ").strip().lower()

if age < 7:
    price = 0
elif age < 18:
    price = 15
elif age >= 65:
    price = 18
else:
    price = 25

# Challenge: a weekend costs 5 zloty more, but children under 7 stay free.
if (day == "saturday" or day == "sunday") and price > 0:
    price = price + 5

if price == 0:
    print("Your ticket is free!")
else:
    print(f"Your ticket costs {price} zloty.")
