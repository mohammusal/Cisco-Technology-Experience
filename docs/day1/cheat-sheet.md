---
hide:
  - navigation
  - toc
---

# Python cheat sheet

<p class="no-print" markdown>Everything from the workshop on one page. Print it with ++ctrl+p++ (on a Mac ++cmd+p++): it fits on one A4 sheet.</p>

<div class="cheat" markdown>

<div markdown>
Virtual environment

```bash
python -m venv .venv         # once
.venv\Scripts\Activate.ps1   # Windows
source .venv/bin/activate    # Mac
deactivate                   # leave
```
</div>

<div markdown>
Print and comments

```python
print("Hello", "Krakow")  # Hello Krakow
# Python skips this line
```
</div>

<div markdown>
Variables and types

```python
age = 16          # int
height = 1.75     # float
name = "Ola"      # str
is_student = True # bool
type(age)         # <class 'int'>
```
</div>

<div markdown>
Maths

```python
7 + 2   # 9      7 - 2   # 5
7 * 2   # 14     7 / 2   # 3.5
7 // 2  # 3      7 % 2   # 1
2 ** 3  # 8      points += 1
```
</div>

<div markdown>
Text and input

```python
name = input("Name? ")
age = int(input("Age? "))
print(f"Hi {name}, {age}!")
"ha" * 3          # 'hahaha'
```
</div>

<div markdown>
Comparisons

```python
5 == 5   # True   5 != 3  # True
5 > 3    # True   5 <= 3  # False
age >= 13 and age <= 19
not True # False
```
</div>

<div markdown>
if / elif / else

```python
if score >= 90:
    print("A")
elif score >= 50:
    print("Pass")
else:
    print("Try again")
```
</div>

<div markdown>
while loop

```python
count = 3
while count > 0:
    print(count)
    count -= 1
```
</div>

<div markdown>
for loop and range

```python
for i in range(5):        # 0 1 2 3 4
    print(i)
range(2, 10, 2)           # 2 4 6 8
range(3, 0, -1)           # 3 2 1
```
</div>

<div markdown>
break and continue

```python
for n in range(10):
    if n == 2:
        continue  # skip 2
    if n == 5:
        break     # stop at 5
```
</div>

<div markdown>
Lists

```python
fruits = ["apple", "kiwi"]
fruits[0]            # 'apple'
fruits[-1]           # 'kiwi'
fruits.append("fig")
fruits.remove("kiwi")
len(fruits)          # 2
```
</div>

<div markdown>
Slices

```python
nums = [0, 1, 2, 3, 4, 5]
nums[1:4]   # [1, 2, 3]
nums[:2]    # [0, 1]
nums[::2]   # [0, 2, 4]
"cisco"[0:3]  # 'cis'
```
</div>

<div markdown>
String methods

```python
" Hi ".strip()      # 'Hi'
"Hi".upper()        # 'HI'
"Hi".lower()        # 'hi'
"a b".split()       # ['a', 'b']
"-".join(["a","b"]) # 'a-b'
```
</div>

<div markdown>
Tuples and sets

```python
point = (3, 4)      # cannot change
point[0]            # 3
seen = {1, 2, 2, 3} # {1, 2, 3}
{1, 2} & {2, 3}     # {2}
```
</div>

<div markdown>
Dictionaries

```python
legs = {"cat": 4, "bird": 2}
legs["cat"]           # 4
legs["fish"] = 0      # add
legs.get("dog", 0)    # 0, no error
for animal in legs: ...
```
</div>

<div markdown>
Random

```python
import random
random.randint(1, 6)       # 1 to 6
random.choice(["a", "b"])
random.sample(my_list, 3)  # 3 different
```
</div>

<div markdown>
Functions

```python
def add(a, b):
    return a + b

add(2, 3)        # 5
add(b=3, a=2)    # 5
```
</div>

<div markdown>
Files

```python
with open("f.txt", "w") as f:  # "a" adds
    f.write("hi\n")
with open("f.txt") as f:
    for line in f:
        print(line.strip())
```
</div>

<div markdown>
Errors: try / except

```python
try:
    n = int("abc")
except ValueError:
    print("Not a number")
finally:
    print("Always runs")
```
</div>

</div>

<p class="cheat-footer" markdown>**Common errors:** `SyntaxError` = typo (missing `:` `)` `"`) · `IndentationError` = wrong spaces · `NameError` = misspelt or undefined name · `TypeError` = wrong type, e.g. `"5" + 1` · `ValueError` = `int("abc")` · `IndexError` = list too short · `KeyError` = key not in dictionary · `ZeroDivisionError` = divided by 0 · `FileNotFoundError` = wrong file name or folder</p>
