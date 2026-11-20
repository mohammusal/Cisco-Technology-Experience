# Lab 1 exercise: pizza party calculator - solution

people = int(input("How many people are coming? "))
slices_each = int(input("How many slices does each person eat? "))
price = 39.90  # zloty for one pizza with 8 slices

slices = people * slices_each
pizzas = (slices + 7) // 8  # adding 7 first makes // round up

print(f"You need {slices} slices.")
print(f"Order {pizzas} pizzas.")
print(f"That costs {round(pizzas * price, 2)} zloty.")
