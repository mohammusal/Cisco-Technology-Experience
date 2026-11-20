# Lab 4: Lists and strings
# Run this file after each TODO. It works even before you change anything.

# TODO 1: A list keeps many values in order.
num_pets = [0, 1, 0, 3, 2, 2]
print(num_pets)
print("Number of students:", len(num_pets))
# Make your own list of 3 favourite foods and print it:
# foods = ["pierogi", "pizza", "zapiekanka"]
# print(foods)

# TODO 2: Indexing. The first item is at index 0. Guess, then remove the #.
cisco = ["c", "i", "s", "c", "o"]
print(cisco[0])
# print(cisco[4])
# print(cisco[-1])
# print(cisco[-3])

# TODO 3: Slicing takes a part: [start:stop]. The stop item is NOT included.
print(cisco[2:5])
# print(cisco[:3])
# print(cisco[3:])
# print(cisco[:])

# TODO 4: Change a list.
letters = ["c", "i", "s"]
letters.append("c")     # add to the end
letters.append("o")
print(letters)
# letters[0] = "C"      # change one item
# del letters[1]        # delete by position
# letters.remove("s")   # delete by value
# print(letters)
# print(letters.index("o"))       # find the position of a value
# print(["a", "b"] + ["c", "d"])  # join two lists

# TODO 5: Loop through a list. enumerate() also gives you the index.
for letter in cisco:
    print(letter)
# for i, letter in enumerate(cisco):
#     print(f"#{i} : {letter}")

# TODO 6: Strings work like lists of letters, but you cannot change them.
wearecisco = "We are Cisco"
print(wearecisco[0])
print(wearecisco[-5:])
# wearecisco[7] = "c"   # remove the #: what error do you get?

# TODO 7: String methods. Guess each result, then remove the #.
# print(wearecisco.upper())
# print(wearecisco.lower())
# print("   lots of space   ".strip())
# print(wearecisco.split())
# print(" *** ".join(["We", "are", "Cisco"]))
# print(wearecisco.replace("Cisco", "awesome!"))
# print(wearecisco.startswith("We"))
# print("are" in wearecisco)
