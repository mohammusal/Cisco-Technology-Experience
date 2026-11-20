# Lab 3 exercise: add up 1 to 100, then FizzBuzz - solution

total = 0
for number in range(1, 101):
    total = total + number
print("1 + 2 + ... + 100 =", total)

# Challenge: FizzBuzz from 1 to 20
for number in range(1, 21):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
