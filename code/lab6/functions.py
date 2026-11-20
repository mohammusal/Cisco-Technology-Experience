# Lab 6: Functions, files and errors
# Run this file after each TODO. It works even before you change anything.

# TODO 1: A function gives a name to a piece of code.
def say_hello():
    print("Hello from a function!")


say_hello()
say_hello()


# TODO 2: Parameters go in, return sends an answer back.
def average(input_list):
    output_average = sum(input_list) / len(input_list)
    return output_average


num_pets = [0, 1, 3, 1, 2]
print(average(num_pets))
# print(average([1, 2, 0]))
# Write your own function square(number) that returns number * number:
# def square(number):
#     return ...
# print(square(5))


# TODO 3: Positional and keyword arguments.
def introduce(name, city, hobby):
    print(f"I am {name} from {city} and I like {hobby}.")


introduce("Ola", "Krakow", "football")                  # positional: by order
# introduce(hobby="chess", name="Jan", city="Gdansk")   # keyword: by name


# TODO 4: int() fails on text that is not a number. try / except catches it.
text = "12"
# text = input("How old are you? ")
try:
    age = int(text)
    print(f"Next year you will be {age + 1}.")
except ValueError:
    print("That is not a whole number.")


# TODO 5: Write a file, then read it back.
with open("notes.txt", "w") as file:
    file.write("Python is fun\n")
    file.write("Krakow is beautiful\n")
# with open("notes.txt") as file:
#     for line in file:
#         print("Read:", line.strip())


# TODO 6: Catch different errors. finally always runs.
a_list = [1, 2, 3]
try:
    result = 3 / 0
    # result = a_list[10]
except ZeroDivisionError:
    print("There was an exception: ZeroDivisionError")
except IndexError:
    print("There was an exception: IndexError")
finally:
    print("This will always be executed")
