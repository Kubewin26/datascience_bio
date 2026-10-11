# Week 3, Day 2: Advanced Functions, Variable Scope & Algorithmic Logic

**Course:** Data Science & Machine Learning (Incubator Hub - DSA 2.0)  
**Instructor:** Israel Odeajo  
**Student:** Winner Kubeyinje (`hswkbioinfo`)  
**Topic:** Keyword Arguments, Arbitrary Arguments (`*args`), Recursion vs. Iteration, Local vs. Global Scope, and Algorithmic Prime Checking.

---

## 1. The Big Picture: Beyond Basic Functions

In our previous class, I learned how to build basic functions using `def`, parameters, and `return`. But real-world data is rarely neat and predictable. 

What if I have arguments and I don't want to worry about their exact left-to-right order? What if a patient arrives with three lab measurements, but another patient arrives with twelve? What happens to variables when a function finishes executing?

This lecture provided the answers:
* **Keyword Arguments** give me order independence.
* **`*args`** gives me dynamic flexibility for variable-length inputs.
* **Scope rules** protect my data from accidental collisions.
* **Recursion** gives me a mathematical way to solve self-repeating problems.

---

## 2. Keyword Arguments: Defeating the Positional Trap

When calling functions positionally, Python strictly matches arguments from left to right. If I get the order wrong, the program doesn't crash, but it produces subtle, dangerous logic bugs.

### The Problem: Positional Disorder
```python
def person(name, gender, age):
    print(f"My name is {name}")
    print(f"I am a {gender}")
    print(f"I am {age} years old.")


# Positional call in the wrong order:
person("Ola", 56, "male")
```
**Output:**
```text
My name is Ola
I am a 56
I am male years old.
```
The computer blindly followed the order: it assigned `56` to `gender` and `'male'` to `age`.

### The Solution: Keyword Syntax (`key = value`)
```python
person(name="Ola", age=56, gender="male")
```
**Output:**
```text
My name is Ola
I am a male
I am 56 years old.
```
By explicitly providing the parameter name as a keyword, order no longer matters. Python routes each value directly to its intended destination.

---

## 3. Arbitrary Arguments (`*args`): The Dynamic Collector

In data science and genomics, we often process datasets of unknown length. If I want to calculate the total dosage or average gene expression across an arbitrary number of replicates, hardcoding parameters like `(x1, x2, x3)` is impossible.

### How `*args` Works:
Placing an asterisk (`*`) before a parameter name tells Python: *"Gather all incoming positional arguments into a single **tuple**."*

```python
def addition(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(addition(3, 5))  # Outputs: 8 (tuple of 2 items)
print(addition(3, 3, 6, 8, 9, 12))  # Outputs: 41 (tuple of 6 items)
```

We can also leverage Python's built-in `sum()` function directly on the tuple:
```python
def adds(*args):
    return sum(args)


print(adds(12, 45, 100))  # Outputs: 157
```

---

## 4. Iteration vs. Recursion (Factorials)

A factorial ($n! = n \times (n-1) \times \dots \times 1$) can be implemented in two fundamentally different ways:

### A. The Iterative Approach (Using a `for` loop)
We loop backwards using `range(start, stop, step)`:
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    answer = 1
    for i in range(n, 0, -1):  # e.g., 5, 4, 3, 2, 1
        answer *= i
    return answer
```

### B. The Recursive Approach (A function calling itself)
A recursive function solves a problem by having the function invoke itself with smaller sub-problems until it hits a termination condition.

```python
def recursive_factorial(n):
    # 1. The Base Case (The Emergency Brake)
    if n == 0 or n == 1:
        return 1
    # 2. The Recursive Case (Self-invocation)
    return n * recursive_factorial(n - 1)
```

### The Rule of Recursion:
A recursive function **must always have a base case**. Without it, Python will enter an infinite loop and throw a `RecursionError: maximum recursion depth exceeded`.

---

## 5. Variable Scope: Local vs. Global Namespace

Scope defines where a variable lives and who has permission to read or modify it.

* **Local Scope:** Variables created inside a function are born when the function is called and die when it finishes. They cannot be seen or altered from outside.
* **Global Scope:** Variables created at the top level of the script or notebook are accessible everywhere.

### Using the `global` Keyword
If a function needs to access or modify a variable in the global namespace without receiving it as a parameter, we use the `global` keyword:

```python
nationality = "Nigerian"


def person(name, age):
    global nationality
    print(f"My name is {name}. I am a {nationality}. I am {age} years old.")


person("Brian", 25)
```

### ⚠️ Diagnosing the Positional Mismatch:
If I accidentally pass `'Ghana'` as a third argument:
```python
person("Feyi", 100, "Ghana")
```
💥 `TypeError: person() takes 2 positional arguments but 3 were given`

*The Takeaway:* `nationality` was pulled directly from the global scope, so the function only expected `name` and `age`. When an error occurs, read the traceback calmly—it explains the exact discrepancy in plain English.

---

## 6. Algorithmic Optimization: Prime Number Sieve

A prime number is only divisible by 1 and itself. Instead of checking every integer from 2 up to $n$, we only need to test up to $\sqrt{n}$ (`int(num ** 0.5) + 1`).

```python
def print_primes_up_to(limit):
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break  # Stop checking as soon as a factor is found
        if is_prime:
            print(num)
```

---

## 7. Cloud Workflows & Recommended Platforms
* **Google Colab (`colab.research.google.com`):** Cloud-hosted Jupyter environment with free CPU/GPU runtimes and integrated AI (Gemini).
* **Practice Hubs:** W3Schools for fast syntax verification, and DataCamp / Rosalind for algorithmic muscle memory.

---

## 8. Biomedical Translation: Clinical & Genomic Mapping

| Classroom Concept | Classroom Example | Biomedical / Clinical AI Equivalent |
| :--- | :--- | :--- |
| **Keyword Arguments** | `person(name='Tom', age=16)` | `assay_sample(patient_id='P-101', dilution=0.05, marker='HER2')` |
| **Arbitrary Arguments (`*args`)** | `addition(*numbers)` | `calculate_mean_expression(*replicates)` (averaging dynamic RNA-seq read counts) |
| **Recursion** | `recursive_factorial(n)` | Navigating phylogenetic tree hierarchies (ancestor-to-descendant traversal) |
| **Local vs. Global Scope** | `global nationality` | Protecting patient privacy: keeping raw clinical identifiers local to the triage function |