# Week 3, Day 1: User-Defined Functions & Modular Program Design

**Course:** Data Science & Machine Learning (Incubator Hub - DSA 2.0)  
**Instructor:** Israel Odeajo  
**Student:** Winner Kubeyinje (`hswkbioinfo`)  
**Topic:** Functions (`def`), Parameters vs. Arguments, Positional Rules, Default Arguments, Loops & Conditionals in Functions, and `return` vs. `print()`.

---

## 1. The Big Picture: Why Do I Need Functions? (The DRY Principle)

Up until now, I have been writing code that executes straight down from top to bottom. If I wanted to calculate a WAEC grade, test an even or odd number, or check blood pressure, I had to write the formula right there on the spot.

But what happens when I have 500 patient records, or when I need to perform the exact same clinical calculation in ten different places in my program?

If I keep copying and pasting the same four lines of code everywhere, I am creating a maintenance nightmare. If there is a bug or if a clinical guideline changes, I would have to hunt down and fix that bug in ten different places.

This is where the **DRY Principle** comes in:
> **DRY: Don't Repeat Yourself.**  
> If you find yourself writing the same logic more than once, bundle it into a **Function**.

### My Mental Model: The Blender Machine
A function is like a kitchen blender:
* It sits on your counter with a name on it: `blender`.
* It has an opening at the top where you drop in fruit: **Parameters / Inputs**.
* It has internal blades that process the fruit according to a fixed recipe: **The Code Block**.
* It pours out a finished smoothie into your cup: **The Return Value / Output**.

You build the blender once, and you can make smoothies a million times with different fruits without ever having to re-invent the blades.

---

## 2. Built-in vs. User-Defined Functions

In Python, functions fall into two clear buckets:

| Category | What It Is | Tools I Have Already Used |
| :--- | :--- | :--- |
| **Built-in Functions** | Tools already baked into Python's standard library by the language creators. | `print()`, `len()`, `type()`, `input()`, `range()`, `sum()`, `max()`, `min()` |
| **User-Defined Functions** | Custom machines **I construct myself** using the `def` keyword to solve my specific business, data science, or biomedical problems. | `additions()`, `numbers()`, `mult()`, `even_numbers()`, `calculate_bmi()` |

---

## 3. The Anatomy of a Function (The 5 Rules of Syntax)

Every user-defined function in Python follows a strict grammatical structure:

```python
def function_name(parameter_1, parameter_2):
    # Indented block of instructions (4 spaces)
    result = parameter_1 + parameter_2
    return result
```

Here is how I break down the anatomy:
1. **`def` (The Declaration):** The reserved keyword telling Python: *"Pay attention, I am defining a new machine."*
2. **Function Name:** A descriptive name written in `snake_case` (lowercase with underscores), e.g., `calculate_gc_content` or `additions`.
3. **Parentheses `()`:** The doorway for inputs. This is where I define any variables the function needs to do its job.
4. **The Colon `:`:** The punctuation mark that terminates the header and tells Python: *"The blueprint is defined; the indented code beneath belongs to this function."*
5. **Indentation (4 Spaces):** Python uses indentation to know what lives inside the function. When the indentation stops, the function ends.

### Crucial Distinction: Defining vs. Calling
* **Defining a function** does **not** run the code! It only registers the recipe in Python's memory.
* **Calling (or invoking) a function** is what actually triggers the execution. You call it by typing its name followed by parentheses: `function_name(arg1, arg2)`.

---

## 4. Parameters vs. Arguments (The Blueprint vs. The Reality)

This is a distinction I want etched into my muscle memory:

* **Parameter (The Placeholder):** The variable name declared inside the function header during definition.  
  * *My Analogy:* An empty cup sitting on a hospital tray labeled `"Patient Blood Sample"`.
  * In `def additions(num1, num2):`, `num1` and `num2` are **parameters**.
* **Argument (The Concrete Value):** The actual, real-world data passed into the function when I invoke it.  
  * *My Analogy:* The actual 5 mL vial of blood placed into that cup when the test runs.
  * In `additions(7, 10)`, `7` and `10` are **arguments**.

---

## 5. Positional Arguments & The 2 Classic `TypeError` Traps

When we pass arguments positionally, Python matches them up one-by-one, in order from left to right. Python enforces an exact count match.

Here is what happens when we violate that contract, exactly as demonstrated by Israel in class:

### The Classroom Multiplication Function:
```python
def mult(num1, num2, num3):
    result = num1 * num2 * num3
    print("The multiple of the three numbers is ", result)
```

### Trap 1: Missing Required Positional Argument
If I call:
```python
mult(5, 9)
```
💥 **Error Output:**
```text
TypeError: mult() missing 1 required positional argument: 'num3'
```
*Why it failed:* Python received values for `num1` (5) and `num2` (9), but slot `num3` was left completely empty. Python refuses to guess.

### Trap 2: Too Many Positional Arguments
If I call:
```python
mult(5, 9, 8, 9)
```
💥 **Error Output:**
```text
TypeError: mult() takes 3 positional arguments but 4 were given
```
*Why it failed:* The machine only has 3 input slots, but I shoved 4 values into it. Python halted execution immediately.

---

## 6. Parameterless Functions: When You Just Need a Fixed Action

A function does not always need inputs. Sometimes you just need an automated routine that performs a fixed task every time it is called:

```python
def word():
    print("welcome to school")


# Calling the parameterless function:
word()
```
**Output:**
```text
welcome to school
```

Even though there are no parameters, the empty parentheses `()` are **mandatory** during both definition and invocation. If you write just `word` without parentheses, Python will only tell you that `word` is a function object; it won't actually run it!

---

## 7. Math & Exponentiation Inside Functions

Functions can perform any mathematical operation. Israel demonstrated squaring numbers using Python's exponentiation operator (`**`):

```python
def double(n):
    result = n**2
    return result


print(double(5))  # Outputs: 25
print(double(10))  # Outputs: 100
```

> [!NOTE]
> Notice the difference between `*` and `**`:  
> `n * 2` is multiplication ($n \times 2$).  
> `n ** 2` is exponentiation ($n^2$).

---

## 8. Conditionals & Loops Inside Functions

A function can hold complete decision trees and iteration loops.

### A. The Even or Odd Classifier (Conditionals)
Using the modulo operator (`%`), which returns the remainder after division:
* If a number divided by 2 has a remainder of 0 (`x % 2 == 0`), it is **even**.
* If the remainder is 1 (`x % 2 == 1`), it is **odd**.

```python
def numbers(x):
    if x % 2 == 0:
        print("The number is even number")
    else:
        print("The number is odd number")


numbers(7)  # Outputs: The number is odd number
numbers(14)  # Outputs: The number is even number
```

### B. Validation & Looping with `range()`
Israel also showed how to validate an input before running a loop:

```python
def even_numbers(n):
    # Guard Clause: Ensure input makes sense
    if n <= 1:
        print("n, should be greater than 1.")
    else:
        # Loop from 1 up to n (using n+1 for half-open interval)
        for num in range(1, n + 1):
            if num % 2 == 0:
                print(num, "This is an even number")
            else:
                print(num, "This is an odd number")


even_numbers(5)
```
**Output:**
```text
1 This is an odd number
2 This is an even number
3 This is an odd number
4 This is an even number
5 This is an odd number
```

---

## 9. Default Parameters (The Safety Net) & The Ordering Rule

Sometimes, an argument is so common that we want to provide a sensible default value so the user doesn't have to specify it every single time.

```python
def best_food(food="Chicken and chips"):
    print("My best food is", food)


# 1. Calling without an argument (uses the default):
best_food()
# Output: My best food is Chicken and chips

# 2. Calling with an argument (overrides the default):
best_food("Garri and Epa")
# Output: My best food is Garri and Epa

best_food("Indomie and Egg")
# Output: My best food is Indomie and Egg
```

### Multiple Default Parameters:
```python
def about_me(name="Israel", food="Chicken and chips"):
    print("My name is", name)
    print("My best food is", food)


about_me()
# Outputs:
# My name is Israel
# My best food is Chicken and chips

about_me("Timileyin", "Eko & Moimoi")
# Outputs:
# My name is Timileyin
# My best food is Eko & Moimoi
```

### ⚠️ The Non-Negotiable Syntax Rule:
Non-default (positional) parameters **must always come first**, followed by default parameters.
* ✅ `def triage(patient_name, status="Stable"):` (Valid!)
* ❌ `def triage(status="Stable", patient_name):` (`SyntaxError: non-default argument follows default argument`)

---

## 10. The Ultimate Trap: `print()` vs. `return`

This is where beginners get tripped up, but I need this clear as daylight:

```python
# Example A: Uses print()
def add_with_print(a, b):
    print(a + b)


# Example B: Uses return
def add_with_return(a, b):
    return a + b
```

What happens when I try to save the result into a variable?
```python
result_a = add_with_print(5, 10)  # Prints 15 to the screen
print("Variable A holds:", result_a)  # Variable A holds: None!

result_b = add_with_return(5, 10)  # Prints nothing to screen
print("Variable B holds:", result_b)  # Variable B holds: 15!
```

### The Core Difference:
* **`print()` is just a projector:** It flashes ink on the screen for human eyes, but the computer cannot catch it. Behind the scenes, the function produces `None`. You cannot do further math with it!
* **`return` is a delivery courier:** It hands the computed value back to Python's memory. You can store it in a variable, pass it into another function, or plot it on a graph.

---

## 11. The Horizon: What Comes Next
Israel previewed where this journey goes next:
1. **Keyword Arguments (`key=value`):** Passing arguments by parameter name so order doesn't matter (e.g. `person(age=25, name="Winner", gender="Male")`).
2. **Flexible Arguments (`*args` and `**kwargs`):** Writing functions that can take an arbitrary number of inputs.
3. **Object-Oriented Programming (OOP):** Creating `class` blueprints that bundle data and functions together.
4. **Transition to Data Analysis:** Moving into `NumPy` and `Pandas` once foundational programming mechanics are mastered.

---

## 12. The Biomedical Bridge: Translating Class Logic to Clinical AI

How does this map to my bioinformatics and clinical research?

| Classroom Concept | Classroom Example | Biomedical / Clinical AI Equivalent |
| :--- | :--- | :--- |
| **Simple Math Function** | `additions(num1, num2)` | `calculate_bmi(weight_kg, height_m)` |
| **Conditional Function** | `numbers(x)` (even/odd) | `triage_glucose(fasting_blood_glucose_mg_dl)` |
| **Function with Loop** | `even_numbers(n)` | `count_gc_content(dna_sequence)` |
| **Default Parameter** | `best_food(food='Chicken and chips')` | `align_sequence(seq, reference='GRCh38')` |
| **Positional Validation** | 3 parameters required | Ensuring mandatory clinical measurements (Systolic, Diastolic, Heart Rate) are never omitted. |