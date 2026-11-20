# Lab 6 exercise: temperature converter and safe division - solution

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def is_hot(celsius):
    return celsius >= 25


for temperature in [-5, 0, 18, 30]:
    fahrenheit = celsius_to_fahrenheit(temperature)
    print(f"{temperature} C = {fahrenheit} F, hot: {is_hot(temperature)}")


# Challenge: a division that never crashes
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You cannot divide by zero!")
        return None


print(safe_divide(10, 2))
print(safe_divide(10, 0))
