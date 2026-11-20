# Lab 5 exercise: a tiny Polish-English dictionary - solution

polish_to_english = {
    "kot": "cat",
    "pies": "dog",
    "smok": "dragon",
    "zamek": "castle",
    "rzeka": "river",
    "dzien dobry": "good morning",
}

word = input("Type a Polish word: ").strip().lower()
print(word, "->", polish_to_english.get(word, "I do not know that word yet"))

# Challenge: count how many times each letter appears in a word
counts = {}
for letter in "krakow":
    if letter in counts:
        counts[letter] = counts[letter] + 1
    else:
        counts[letter] = 1
print(counts)
