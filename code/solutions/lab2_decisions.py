# Lab 2: Making decisions - solution

print(5 > 3)
print(5 == 5.0)
print("cat" == "Cat")
print(10 != 10)

sunny = True
weekend = False
print(sunny and weekend)
print(sunny or weekend)
print(not weekend)

age = 16
if age >= 15:
    print("You can watch the film.")
else:
    print("Sorry, this film is for 15 and older.")

score = 75
if score >= 95:
    grade = 6
elif score >= 85:
    grade = 5
elif score >= 70:
    grade = 4
elif score >= 50:
    grade = 3
elif score >= 30:
    grade = 2
else:
    grade = 1
print(f"A score of {score} gives grade {grade}")

is_weekend = True
if is_weekend:
    print("No school today.")
    print("Have fun!")
