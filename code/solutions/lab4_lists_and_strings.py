# Lab 4: Lists and strings - solution

num_pets = [0, 1, 0, 3, 2, 2]
print(num_pets)
print("Number of students:", len(num_pets))
foods = ["pierogi", "pizza", "zapiekanka"]
print(foods)

cisco = ["c", "i", "s", "c", "o"]
print(cisco[0])
print(cisco[4])
print(cisco[-1])
print(cisco[-3])

print(cisco[2:5])
print(cisco[:3])
print(cisco[3:])
print(cisco[:])

letters = ["c", "i", "s"]
letters.append("c")
letters.append("o")
print(letters)
letters[0] = "C"
del letters[1]
letters.remove("s")
print(letters)
print(letters.index("o"))
print(["a", "b"] + ["c", "d"])

for letter in cisco:
    print(letter)
for i, letter in enumerate(cisco):
    print(f"#{i} : {letter}")

wearecisco = "We are Cisco"
print(wearecisco[0])
print(wearecisco[-5:])

print(wearecisco.upper())
print(wearecisco.lower())
print("   lots of space   ".strip())
print(wearecisco.split())
print(" *** ".join(["We", "are", "Cisco"]))
print(wearecisco.replace("Cisco", "awesome!"))
print(wearecisco.startswith("We"))
print("are" in wearecisco)
