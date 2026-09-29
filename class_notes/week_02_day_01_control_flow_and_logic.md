# Week 2, Day 1: Control Flow, Boolean Logic & Program Decisions

**Course:** Data Science & Machine Learning (Incubator Hub - DSA 2.0)  
**Instructor:** Israel Odeajo  
**Student:** Winner Kubeyinje (`hswkbioinfo`)  

---

## 1. What is Control Flow?

Normally, Python reads code from top to bottom, line by line.  
**Control Flow** allows a program to make smart decisions: to choose which lines of code to run, which lines to skip, or which lines to repeat based on real-time data.

* *Real-world analogy:* When you open your banking app, it doesn't immediately transfer money. It first checks: *"Is your password correct?"* If yes, you log in. If no, you are locked out.

---

## 2. Anatomy of an `if` Statement: Condition vs. Block

Every decision in Python has two parts:

1. **The Condition (The Gatekeeper):**  
   A test that evaluates to either `True` or `False`.
2. **The Block of Code (The Action):**  
   The indented instructions that run *only* if the condition is `True`.

```python
age = 10

if age >= 18:
    print("You are an adult")
else:
    print("You are young")
```

### The Two Golden Syntax Rules:
* **The Colon (`:`):** Every `if`, `elif`, and `else` line **must** end with a colon. It tells Python: *"The rule is defined; the indented code beneath me belongs to this decision."*
* **Indentation (4 spaces):** Python uses indentation instead of curly brackets `{ }`. Everything indented by 4 spaces runs inside that block.

---

## 3. Comparison Operators (The Raw Evidence)

Comparison operators compare two values and always return a Boolean (`True` or `False`):

| Operator | Meaning | Example | Evaluates To |
| :---: | :--- | :--- | :---: |
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `10 > 18` | `False` |
| `<` | Less than | `7 < 9` | `True` |
| `>=` | Greater than or equal to | `18 >= 18` | `True` |
| `<=` | Less than or equal to | `10 <= 5` | `False` |

> ⚠️ **Case Sensitivity Reminder:**  
> Python is strictly case-sensitive. `'age' == 'Age'` evaluates to **`False`** because of the capital `'A'`.

---

## 4. The 3 Boolean Logic Gates: `and`, `or`, `not`

Often, a decision requires checking multiple conditions at once:

### A. `and` (Strict Conjunction — The "Taiwo & Kehinde" Rule)
* **Rule:** Evaluates to `True` **only if EVERY condition is `True`**. If even one is `False`, the entire line is `False`.
* *Example:* For twins, you need both *Taiwo AND Kehinde*.
* `(5 > 3) and (4 < 5)` $\rightarrow$ `True and True` $\rightarrow$ **`True`**
* `(5 > 3) and (4 < -5)` $\rightarrow$ `True and False` $\rightarrow$ **`False`**

### B. `or` (Disjunction — The "Boy or Girl" Rule)
* **Rule:** Evaluates to `True` if **AT LEAST ONE condition is `True`**.
* *Example:* Whether you have a boy OR a girl, you celebrate!
* `(5 > 3) or (4 < -5)` $\rightarrow$ `True or False` $\rightarrow$ **`True`**
* `(5 < 3) or (4 < -20)` $\rightarrow$ `False or False` $\rightarrow$ **`False`**

### C. `not` (The Inverter & The Parentheses Cheat Code)
* **Rule:** Reverses the Boolean value. `not True` becomes `False`; `not False` becomes `True`.
* 🔑 **The Cheat Code:** *Never distribute `not` into parentheses! Solve whatever is inside the parentheses first down to a single `True` or `False`. Then apply `not` at the very end.*
* *Example:* `not(10 > 5 and 3 < 1)`
  * Step 1 (Inside parentheses): `10 > 5` is `True`, `3 < 1` is `False`. `True and False` = `False`.
  * Step 2 (Apply `not`): `not(False)` = **`True`**!

---

## 5. The Modulus Operator (`%`): Finding Remainders

The `%` symbol calculates the **integer remainder** after division:
* Normal division (`/`): `9 / 2 = 4.5`
* Modulus (`%`): `9 % 2 = 1` *(2 goes into 9 four times, with 1 left over)*

### Detecting Even vs. Odd Numbers:
* If a number is divided by 2 and has **0 remainder**, it is **Even**:
  ```python
  num = 8
  if num % 2 == 0:
      print(num, "is even")
  else:
      print(num, "is odd")
  ```

---

## 6. Nested `if` Statements: Hierarchical Decision Trees

A **nested `if`** is simply an `if` placed inside another `if`:
```python
a = 3

if a >= 0:
    # This inner check only runs if 'a' is zero or positive
    if a % 2 == 0:
        print(a, "is even")
    else:
        print(a, "is odd")
else:
    print(a, "is negative")
```
* *Connection to AI:* This is the exact logic behind **Decision Trees** and **Random Forests** in Machine Learning (evaluating features step by step).

---

## 7. Multi-Tier Grading with `if / elif / else`

When you have more than two outcomes, use `elif` ("else if"):
* Python tests conditions **from top to bottom**.
* The **first condition that is `True` executes its block and immediately stops the rest of the chain**.

```python
score = 79

if score < 40:
    grade = "FAIL"
elif score < 55:
    grade = "PASS"
elif score < 70:
    grade = "MERIT"
elif score <= 100:
    grade = "DISTINCTION"
else:
    grade = "INVALID SCORE"

print("grade:", grade)  # Prints: grade: DISTINCTION
```

> 💡 **The Golden Order Rule:**  
> When checking with greater-than-or-equal (`>=`), **always check from the highest number down to the lowest number!**  
> If you test `score >= 50` before `score >= 75`, a student with 85 marks will get trapped in the 50 block and receive the wrong grade!