# Lab 2: Making decisions
# Run this file after each TODO. It works even before you change anything.

# TODO 1: Comparisons give True or False. Guess each answer, then remove the #.
# print(5 > 3)
# print(5 == 5.0)
# print("cat" == "Cat")
# print(10 != 10)

# TODO 2: Combine with and, or, not. Guess first!
sunny = True
weekend = False
# print(sunny and weekend)
# print(sunny or weekend)
# print(not weekend)

# TODO 3: if / else. Change age and run it twice: once with 12, once with 16.
age = 12
if age >= 15:
    print("You can watch the film.")
else:
    print("Sorry, this film is for 15 and older.")

# TODO 4: elif. Turn a test score (0-100) into a Polish school grade (1-6).
score = 75
if score >= 95:
    grade = 6
elif score >= 85:
    grade = 5
# Add more elif lines here: 70 or more -> 4, 50 or more -> 3, 30 or more -> 2
else:
    grade = 1
print(f"A score of {score} gives grade {grade}")

# TODO 5: Indentation. Lines with the same spaces belong together.
# Fix the line marked BROKEN so the program prints "Have fun!" only on weekends.
is_weekend = True
if is_weekend:
    print("No school today.")
print("Have fun!")  # BROKEN: move this line inside the if (4 spaces)
