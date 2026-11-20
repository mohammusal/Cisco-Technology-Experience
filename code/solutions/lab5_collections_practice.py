# Lab 5: Tuples, dictionaries and sets - solution

position = (3, 4)
print("x is", position[0], "and y is", position[1])
names = ["Ola", "Jan", "Zosia"]
scores = [7, 9, 8]
for pair in zip(names, scores):
    print(pair)

legs = {"cat": 4, "bird": 2, "spider": 8}
print(legs["spider"])
legs["fish"] = 0
legs["bird"] = 2
print(legs)
print(len(legs), "animals")
print(legs.get("dog", "unknown"))
for animal in legs:
    print(f"A {animal} has {legs[animal]} legs")
print("cat" in legs)

visitors = {"Ola", "Jan", "Ola", "Zosia", "Jan"}
print(visitors)
print(len(visitors), "different visitors")
monday = {"Ola", "Jan", "Kuba"}
tuesday = {"Jan", "Zosia", "Kuba"}
print(monday & tuesday)
print(monday | tuesday)
print(monday - tuesday)
