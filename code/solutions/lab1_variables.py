# Lab 1: Variables, types and operators - solution

name = "Ola"
age = 15
city = "Krakow"
print(name)
print(age)
print(city)

print(type(name))
print(type(age))
print(type(1.75))
print(type(True))

pocket_money = 50
weeks = 4
total = pocket_money * weeks
print("In", weeks, "weeks I get", total, "zloty")
print(17 / 5)
print(17 // 5)
print(17 % 5)
print(2 ** 10)

print("Hello, " + name + "!")
print("I am " + str(age) + " years old")
print(f"I am {age} years old")

year = input("Which year were you born? ")
age_next_year = 2027 - int(year)
print(f"In 2027 you will be {age_next_year}.")
