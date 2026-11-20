# Lab 6: Functions, files and errors - solution

def say_hello():
    print("Hello from a function!")


say_hello()
say_hello()


def average(input_list):
    output_average = sum(input_list) / len(input_list)
    return output_average


num_pets = [0, 1, 3, 1, 2]
print(average(num_pets))
print(average([1, 2, 0]))


def square(number):
    return number * number


print(square(5))


def introduce(name, city, hobby):
    print(f"I am {name} from {city} and I like {hobby}.")


introduce("Ola", "Krakow", "football")
introduce(hobby="chess", name="Jan", city="Gdansk")

text = input("How old are you? ")
try:
    age = int(text)
    print(f"Next year you will be {age + 1}.")
except ValueError:
    print("That is not a whole number.")

with open("notes.txt", "w") as file:
    file.write("Python is fun\n")
    file.write("Krakow is beautiful\n")
with open("notes.txt") as file:
    for line in file:
        print("Read:", line.strip())

a_list = [1, 2, 3]
try:
    result = a_list[10]
except ZeroDivisionError:
    print("There was an exception: ZeroDivisionError")
except IndexError:
    print("There was an exception: IndexError")
finally:
    print("This will always be executed")
