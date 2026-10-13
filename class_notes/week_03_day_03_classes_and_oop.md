# Week 3, Day 3: Object-Oriented Programming (OOP) & Classes

**Course:** Data Science & Machine Learning (Incubator Hub - DSA 2.0)  
**Instructor:** Israel Odeajo  
**Student:** Winner Kubeyinje (`hswkbioinfo`)  

---

## 1. What is Object-Oriented Programming (OOP)?

Until today, we wrote procedural code: we created loose variables (like `name = "Ada"`, `age = 15`, `grade = 10`) and wrote functions that took those variables from the outside. That works when you only have a few variables, but when you have 100 students or 1,000 biological patient samples, managing loose variables becomes messy and easy to mix up.

**Object-Oriented Programming (OOP)** is simply bundling data (attributes) and the actions performed on that data (methods) together into a single, self-contained unit.

### The Core Analogy: The Blank Form vs. The Living Person
* **A Class is a blank form (the blueprint):** It defines what fields need to be filled in (like Name, Age, Grade) and what actions can be taken. The blank paper itself has no identity—you cannot ask a blank form to introduce itself.
* **An Object is a filled-out form (the living instance):** When Ada walks in and fills out the form, she becomes a real entity sitting in memory.
* **Why do we store it in a variable (`student1 = Student(...)`)?** The variable `student1` is our handle to that specific person. If we just wrote `Student.introduce()`, Python throws an error because the blank form on the shelf has no name or age to speak of.

---

## 2. Everything in Python is Already an Object

One of the biggest eye-openers from today's lecture:
```python
fruit = "Banana"
print(type(fruit))  # Outputs: <class 'str'>
```
Even simple text belongs to a class (`str`). Because `"Banana"` is an object of the `str` class, it already comes with built-in actions attached to it, like `fruit.upper()` or `fruit.count("a")`. Today, we learned how to design our own custom classes.

---

## 3. The Anatomy of a Class: `__init__`, `self`, and Methods

### A. Creating a Blank Class
```python
class Person:
    pass


p = Person()
print(p)  # Outputs: <__main__.Person at 0x...>
```
* `class`: The keyword to define a blueprint. Class names use `PascalCase` (CapitalizedWords).
* `pass`: A placeholder so Python doesn't throw an indentation error.
* `0x...`: The unique memory address where this object lives in computer RAM.

### B. The Constructor (`__init__`) — The Front Desk
```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
```
* `__init__`: Short for *initialize*. It runs automatically the very millisecond a new object is created.
* It takes the answers given at the door and attaches them to that student's record.
* If you call `Student()` without passing the required arguments, Python immediately throws a `TypeError: missing required positional arguments`.

### C. What is `self`? (The Personal Badge)
* `self` is the first parameter of every method inside a class.
* When Ada introduces herself, `self.name` refers to *Ada's own name*. When John introduces himself, `self.name` refers to *John's own name*.
* Python passes `self` automatically in the background. You never type `self` when creating or calling an object.

### D. Attributes vs. Methods (Nouns vs. Verbs)
* **Attributes (Nouns):** Facts stored on the object's badge (e.g., `car1.color`, `car1.speed`). Accessed **without** parentheses.
* **Methods (Verbs):** Actions the object knows how to perform (e.g., `car1.accelerate()`). Invoked **with** parentheses `()`.

---

## 4. In-Class Coding Drills & Verification

All three drills given by Israel were coded, tested, and verified inside `notebooks/02_functions_practice_lab.ipynb`:

### Drill 1: The Student Class (Attributes & String Formatting)
```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print(
            f"My name is {self.name}, I am {self.age} years old, and I am in grade {self.grade}."
        )


student1 = Student("Ada", 15, 10)
student2 = Student("John", 16, 11)

student1.introduce()
student2.introduce()
```
**Output:**
```text
My name is Ada, I am 15 years old, and I am in grade 10.
My name is John, I am 16 years old, and I am in grade 11.
```

### Drill 2: The Rectangle Class (Calculated Returns)
```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculateArea(self):
        return self.length * self.width


rect1 = Rectangle(5, 3)
rect2 = Rectangle(10, 4)

print(
    f"A rectangle with length {rect1.length} and width {rect1.width} should have an area of {rect1.calculateArea()}."
)
print(
    f"A rectangle with length {rect2.length} and width {rect2.width} should have an area of {rect2.calculateArea()}."
)
```
**Output:**
```text
A rectangle with length 5 and width 3 should have an area of 15.
A rectangle with length 10 and width 4 should have an area of 40.
```

### Drill 3: The Car Class (State Mutation & Encapsulation)
```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0  # Speed starts at 0 by default for every car

    def accelerate(self):
        self.speed += 10

    def showDetails(self):
        print(
            f"Brand: {self.brand}, Color: {self.color}, Current Speed: {self.speed} km/h"
        )


car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

car1.accelerate()
car1.accelerate()

print(
    f"The first car's speed should be {car1.speed} km/h, and the second car's speed should still be {car2.speed} km/h."
)
car1.showDetails()
car2.showDetails()
```
**Output:**
```text
The first car's speed should be 20 km/h, and the second car's speed should still be 0 km/h.
Brand: Toyota, Color: Red, Current Speed: 20 km/h
Brand: Honda, Color: Blue, Current Speed: 0 km/h
```
* **Key Takeaway:** Demonstrates that each object remembers its own state. Accelerating `car1` twice updated its speed to `20 km/h` without affecting `car2`, which remained stationary at `0 km/h`.

---

## 5. Why This Matters for Data Science & Bioinformatics

* **In Machine Learning (Scikit-Learn):** Every model is a class (e.g., `model = LinearRegression()`). The `model.fit(X, y)` method trains the model by updating its internal state, and `model.predict(X_test)` generates predictions using that internal state.
* **In Bioinformatics:** Rather than storing patient IDs, chromosome names, mutation counts, and raw DNA strings in disconnected variables, we can bundle them into a single `PatientSample` or `DNASequence` object that manages its own GC content calculations and variant lookups.