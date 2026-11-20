# Lab 5: Tuples, dictionaries and sets
# Run this file after each TODO. It works even before you change anything.

# TODO 1: A tuple is like a list that can never change.
position = (3, 4)
print("x is", position[0], "and y is", position[1])
# position[0] = 10   # remove the #: what error do you get?
names = ["Ola", "Jan", "Zosia"]
scores = [7, 9, 8]
for pair in zip(names, scores):  # zip makes tuples from two lists
    print(pair)

# TODO 2: A dictionary looks up a value by its key, like the contacts in a phone.
legs = {"cat": 4, "bird": 2, "spider": 8}
print(legs["spider"])
legs["fish"] = 0          # add a new key and value
legs["bird"] = 2          # change a value
print(legs)
print(len(legs), "animals")
# print(legs["dog"])        # remove the #: what error do you get?
# print(legs.get("dog", "unknown"))
# for animal in legs:
#     print(f"A {animal} has {legs[animal]} legs")
# print("cat" in legs)

# TODO 3: A set keeps only unique values.
visitors = {"Ola", "Jan", "Ola", "Zosia", "Jan"}
print(visitors)
print(len(visitors), "different visitors")
# monday = {"Ola", "Jan", "Kuba"}
# tuesday = {"Jan", "Zosia", "Kuba"}
# print(monday & tuesday)   # in both
# print(monday | tuesday)   # in either
# print(monday - tuesday)   # only on Monday
