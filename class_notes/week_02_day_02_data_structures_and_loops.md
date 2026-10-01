# Week 2, Day 2: Python Data Structures (Collections) & Loops

**Course:** Data Science & Machine Learning (Incubator Hub - DSA 2.0)  
**Instructor:** Israel Odeajo  
**Student:** Winner Kubeyinje  

---

## 1. What are Data Structures (Collections)?

In real-world data science, we work with groups of related data (like hundreds of patient records, gene measurements, or test scores).  
A **collection** allows us to store many values inside a single named container.

Python has **4 core collections**:
1. **Tuples** `()` — Ordered, cannot be changed (immutable).
2. **Lists** `[]` — Ordered, can be changed (mutable).
3. **Sets** `{}` — Unordered, unique values only (no duplicates).
4. **Dictionaries** `{key: value}` — Named mappings (look up values by label).

---

## 2. Tuples `()` — The Sealed Container (Immutable)

A tuple is defined using **round brackets `()`**:
```python
coordinates = (1.2, -0.3, 0.9)
patient = ("PT_101", 45, True)
```

### Key Properties:
* **Ordered:** Every element has a fixed position starting at index 0.
* **Immutable:** Once created, you **cannot** update, add, or delete any item.
  ```python
  t = (10, 20, 30)
  t[0] = 99  # CRASH! TypeError: 'tuple' object does not support item assignment
  ```
* **Packing & Unpacking:**
  ```python
  # Packing:
  t = 2, 3, 4

  # Unpacking:
  a, b, c = t
  print(a, b, c)  # Prints: 2 3 4
  ```

---

## 3. Lists `[]` — The Editable Rack (Mutable)

A list is defined using **square brackets `[]`**:
```python
ages = [24, 45, 62, 19]
mixed = [1, "Ola", 98.6, True]
empty = []
```

### Key Properties:
* **Ordered:** Fixed positions starting at index 0.
* **Mutable:** You can change values directly!
  ```python
  x = [321, 45, 29]
  x[0] = 222  # Successfully updates 321 to 222!
  ```

### Converting Between Tuples and Lists:
* `list((1, 2, 3))` $\rightarrow$ converts tuple to list `[1, 2, 3]`.
* `tuple([1, 2, 3])` $\rightarrow$ converts list to tuple `(1, 2, 3)`.

### 2D Matrices and Keyboard Inputs:
```python
matrix = [[int(input()), int(input())], [int(input()), int(input())]]
```
* `input()` takes user keystrokes from the terminal.
* `int(input())` converts the entered text into a whole number.

---

## 4. Indexing & Slicing (The Half-Open Interval)

### Indexing (Single Position):
* **Index ALWAYS starts at 0!**
```python
# Values:   [ 321,   45,   29,   78,   30 ]
# Index:       0      1     2     3     4
x = [321, 45, 29, 78, 30]

print(x[0])  # 321 (First item)
print(x[1])  # 45  (Second item)
```

### Slicing Ranges `[start:end]` (Half-Open Interval $[start, end)$):
* **The `end` position is ALWAYS EXCLUDED!**
* **Number of items returned** $= end - start$.

```python
x[1:4]  # Takes index 1, 2, 3 -> [45, 29, 78] (4 - 1 = 3 items)
x[:3]  # Starts at 0, takes index 0, 1, 2 -> [321, 45, 29] (3 items)
x[2:]  # Starts at index 2 till the end -> [29, 78, 30]
```

---

## 5. Essential List Methods

| Method | What It Does | Example | Output |
| :--- | :--- | :--- | :--- |
| `len(x)` | Total count of elements | `len([10, 20, 30])` | `3` |
| `x.count(val)` | Counts occurrences of `val` | `[5, 5, 2].count(5)` | `2` |
| `x.append(val)` | Adds 1 item to the very end | `x.append(101)` | `[..., 101]` |
| `x.insert(pos, val)`| Adds item at a specific index | `x.insert(1, 999)` | Puts 999 at index 1 |
| `x.remove(val)` | Removes first item matching `val` | `x.remove(45)` | Deletes 45 |
| `del x[pos]` | Deletes item at index `pos` | `del x[0]` | Deletes index 0 |
| `sorted(x)` | Returns new list in ascending order | `sorted([4, 1, 3])` | `[1, 3, 4]` |

> ⚠️ **The Append vs. Extend Trap:**
> * `a.extend([4, 5])` $\rightarrow$ adds 4 and 5 as separate items: `[1, 2, 3, 4, 5]`. (Same as `a + [4, 5]`).
> * `a.append([4, 5])` $\rightarrow$ adds the list as a single nested box: `[1, 2, 3, [4, 5]]`.

---

## 6. Sets `{}` — The Duplicate Eliminator

Defined using **curly braces `{}`** or `set()`:
```python
raw_samples = [1, 2, 3, 2, 3]
unique_set = set(raw_samples)
print(unique_set)  # {1, 2, 3} (Duplicates removed automatically!)
```

### Key Properties:
* **Unique:** No repeated items allowed.
* **Unordered:** Items have no fixed index (`s[0]` is not allowed).
* **Set Operations:**
  * **Union (`|`):** Combines both sets without repeats:  
    `{2, 4} | {4, 6}` $\rightarrow$ `{2, 4, 6}`
  * **Intersection (`&`):** Finds elements common to both sets:  
    `{2, 4} & {4, 6}` $\rightarrow$ `{4}`

---

## 7. Dictionaries `{key: value}` — "The King of Them All"

A dictionary stores data as **Key-Value pairs** using **curly braces `{}`**:
```python
bio_data = {"name": "Ola", "age": 18, "email": "ola89@gmail.com", "salary": 56.80}
```

### Accessing & Defending Against Crashes:
* Direct lookup: `bio_data["name"]` $\rightarrow$ `"Ola"`.
* If a key doesn't exist: `bio_data["blood_group"]` crashes with `KeyError`!
* **The Defensive Fix (`.get()`):**
  ```python
  bio_data.get("blood_group")  # Returns None (No crash!)
  bio_data.get("blood_group", "Unknown")  # Returns "Unknown" (Safe default!)
  ```

### Inspecting Dictionaries:
* `bio_data.keys()` $\rightarrow$ lists all keys.
* `bio_data.values()` $\rightarrow$ lists all values.
* `bio_data.items()` $\rightarrow$ lists all key-value pairs as tuples.

---

## 8. Loops — Automated Repetition

### A. The `while` Loop (Condition-driven):
Repeats as long as a condition is `True`. Needs an initialization and an increment:
```python
x = 5
while x <= 10:
    print(x)
    x += 1  # MUST increment, otherwise loop runs forever!
```

#### Loop Control Valves:
* **`break` (Emergency Exit):** Exits the loop immediately.
* **`continue` (Skip Button):** Skips the current round and jumps right back to the top for the next round.

### B. The `for` Loop (Sequence-driven):
Iterates directly through any collection:
```python
# Over a list:
for color in ["red", "blue", "green"]:
    print(color)

# Over a string:
for char in "Brian":
    print(char)

# Over a range of numbers (excluding the end):
for i in range(1, 6):
    print(i)  # Prints 1, 2, 3, 4, 5
```

### C. Number Guessing Game (Class Exercise):
```python
chosen_number = 8
num_chances = 6

for i in range(num_chances):
    user_guess = int(input("Guess my chosen number between 1 and 20: "))
    if user_guess == chosen_number:
        print("Congratulations! You guessed my chosen number!")
        break
    elif user_guess > chosen_number:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
```