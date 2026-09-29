# Week 1, Day 2: Python Basics, Data Types & Course Materials Import

**Course:** Data Science & Machine Learning (Incubator Hub - DSA 2.0)  
**Instructor:** Israel Odeajo  
**Student:** Winner Kubeyinje (`hswkbioinfo`)  

---

## 1. What is a Variable? (The Memory Container Analogy)

In computer programming, a **variable** is simply a labeled storage box in the computer's memory.
* You create a label on the box (the variable name).
* You place a piece of data inside the box (the value).

```python
# Putting the value "Ola" inside a container labeled 'name'
name = "Ola"

# Putting the number 10 inside a container labeled 'age'
age = 10
```

To see what is inside the box, we use the `print()` function:
```python
print(name)  # Outputs: Ola
print(age)  # Outputs: 10
```

---

## 2. The 4 Fundamental Primitive Data Types

Every piece of data stored in Python belongs to a specific "type":

| Data Type | Python Keyword | What It Is | Examples |
| :--- | :--- | :--- | :--- |
| **String** | `str` | Text wrapped in quotes (`""` or `''`) | `"Ola"`, `"Male"`, `"BRCA1"` |
| **Integer** | `int` | Whole numbers (positive or negative, no decimals) | `10`, `45`, `-3`, `150000` |
| **Float** | `float` | Real numbers that have a decimal point | `120.5`, `98.6`, `7.35` |
| **Boolean** | `bool` | Binary truth values (Only two choices: `True` or `False`) | `True`, `False` |

---

## 3. The "Quote Trap" & Type Casting

This is one of the most common traps for beginners in data science:

### The Rule:
If you put quotation marks around digits, **Python treats it as text (a string), not a number!**

```python
val_a = "40"  # This is a STRING (text) because of the quotes
val_b = 40  # This is an INTEGER (a real number)
```

### Why This Is Dangerous (Concatenation vs. Addition):
* **When you add two numbers:** `40 + 40` gives **`80`** (mathematical addition).
* **When you add two strings:** `"40" + "40"` gives **`"4040"`** (joining text together, called **concatenation**).
* **When you multiply a string:** `"40" * 2` gives **`"4040"`** (it repeats the text twice!).

### How to Fix It (Type Casting):
We can convert strings into numbers using Python's conversion functions:
* `int("40")` $\rightarrow$ converts the text `"40"` into the integer `40`.
* `float("120.5")` $\rightarrow$ converts the text `"120.5"` into the decimal number `120.5`.
* `str(40)` $\rightarrow$ converts the number `40` back into the text `"40"`.

---

## 4. The Rules for Naming Variables

When creating variable names, Python has strict grammar rules:

* ✅ **Allowed (Legal):**
  * `patient_1` (letters, numbers, and underscores)
  * `patient_age` (using snake_case)
  * `score`
* ❌ **Not Allowed (Will crash with SyntaxError):**
  * `patient 1` (Cannot have spaces! Python thinks they are two separate commands).
  * `patient-1` (Cannot use hyphens! Python thinks you are trying to subtract 1).
  * `1_patient` (Cannot start with a number).

### Case Sensitivity:
Python is strictly **case-sensitive**. Capital letters and lowercase letters are treated as completely different things:
* `age`, `Age`, and `AGE` are three completely different variables in memory.
* `"age" == "Age"` evaluates to **`False`**.

---

## 5. Action (`=`) vs. Question (`==`)

One of the most important operator distinctions in programming:

* **Single Equal Sign (`=`): An Action (Assignment)**  
  It stores a value into a container.  
  `tumor_stage = "Stage II"` *(Action: Put "Stage II" inside tumor_stage)*

* **Double Equal Sign (`==`): A Question (Equality Check)**  
  It asks the computer: *"Are these two things identical?"* It always returns `True` or `False`.  
  `tumor_stage == "Stage II"` *(Question: Is tumor_stage equal to "Stage II"? $\rightarrow$ Returns `True`)*

---

## 6. Hands-on Milestone: Importing the Full 16-Week Course Syllabus

On Day 2, we imported all the official course materials provided by the instructor into our WSL environment and established version control protection:

1. **Large File Protection (`.gitignore`):**
   * We discovered that the course materials included a massive dataset: `boston_311_calls.csv` (526 Megabytes!).
   * GitHub has a strict limit of 100 MB per file. Pushing a 526 MB file would lock the repository.
   * We added `*.csv` to our `.gitignore` file, telling Git to safely ignore all CSV files.
2. **Transferring Course Materials into WSL:**
   * We unzipped the course package in Windows Downloads and copied all 23 curriculum items directly into:
     `~/datascience_bio/DSA_syllabus/`
3. **Pushed 208 Curriculum Objects to GitHub:**
   * We verified that Git tracked all notebooks and documents while completely ignoring the 526 MB CSV file.
   * We committed and pushed cleanly over SSH (commit `c9f790d`).