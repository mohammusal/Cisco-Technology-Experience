# Lab 4 exercise: username generator - solution

first = input("First name: ").strip().lower()
last = input("Last name: ").strip().lower()
year = input("Year you were born: ").strip()

username = first[:3] + last[:3] + year[-2:]
print("Your username is:", username)

# Challenge: count the vowels in your full name
vowels = 0
for letter in first + last:
    if letter in "aeiouy":
        vowels = vowels + 1
print("Vowels in your name:", vowels)
