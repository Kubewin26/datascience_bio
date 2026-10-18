# Week 4, Day 1: Advanced OOP — Encapsulation & Inheritance

**Course:** Data Science & Machine Learning (Incubator Hub - DSA 2.0)  
**Instructor:** Israel Odeajo  
**Student:** Winner Kubeyinje (`hswkbioinfo`)  

---

## 1. Executive Summary & Reflective Voice (Winner Kubeyinje)

Today's session pushes deeper into Object-Oriented Programming (OOP) by focusing on two of its four core pillars: **Encapsulation** and **Inheritance** (with Abstraction and Polymorphism concluding our OOP foundation).

Until now, I understood how to design a basic class blueprint and instantiate objects. Today's major shift is learning **how to protect sensitive internal data from unintended tampering (Encapsulation)** and **how to build specialized classes efficiently without duplicating code (Inheritance)**.

My key practical takeaway today:
1. **Encapsulation is about guardrails, not an absolute padlock.** In Python, prefixing an attribute with an underscore (like `_base_salary`) signals to other developers: *"This is internal engine wiring—do not modify or rely on this directly from the outside."* If an attribute needs updating, we provide official setter methods (like `setBaseSalary()`) where validation rules can safely protect data integrity.
2. **Inheritance is like stapling an extra page to an existing identity form.** Rather than creating a new `Student` or `Employee` form from scratch and re-writing basic fields like `name`, `age`, and `gender`, we inherit those 4 fields and the `ID_card()` method directly from the parent `Person` class, only writing the additional attributes unique to that role.
3. **The distinction between `return` and `print` in class methods:** `_calculate_salary(self)` acts like a silent accountant doing math and returning a raw numeric value internally, while `generate_payslip(self)` acts like the printer displaying the final formatted text to human eyes.

---

## 2. Core Concepts: The 50-Year Expert Breakdown

### A. Encapsulation: Protecting State & Preventing Data Corruption
* **The Problem:** If attributes are public, any external script can alter them (e.g., `emp1.base_salary = -50000`), breaking company payroll or clinical dosage pipelines.
* **The Python Convention:** Prefixing variables and methods with a single underscore (`_` or `__`) designates them as private.
* **The Danger of Reading Private Variables:** Even harmless operations like `print(emp1._base_salary)` are dangerous because internal wiring can be refactored by the architect at any time. Relying on private internals causes external code to break unexpectedly.
* **Setters & Getters:** Safe methods provided by the class author to read or adjust private attributes under controlled conditions.

### B. Inheritance: Maximizing Code Reusability (DRY)
* **Parent / Super / Base Class:** The general template containing shared attributes and behaviors (e.g., `Person`).
* **Child / Sub / Derived Class:** The specialized template that inherits all parent attributes and methods (e.g., `Employee(Person)` and `Student(Person)`).
* **The Constructor Handshake:** Inside the child's `__init__`, we call `Person.__init__(self, name, age, gender, ID)` (or `super().__init__(...)`) to let the parent initialize the standard fields, avoiding repetitive code.

---

## 3. Practical Coding Drills & Verification

Both drills were coded, executed, and verified inside `notebooks/02_functions_practice_lab.ipynb`:

### Drill 1: Encapsulation (Secure Employee Class)
```python
class Employee:
    # Private class variable (Company baseline)
    _base_salary = 50000

    def __init__(self, name, level, position):
        self.name = name
        self.level = level
        self.position = position

    # Private calculation method (Silent accountant)
    def _calculate_salary(self):
        return Employee._base_salary + (Employee._base_salary * (self.level / 10))

    # Public method (Formatted payslip display)
    def generate_payslip(self):
        print(
            f"Name: {self.name} \nPosition: {self.position} \nLevel: {self.level} \nSalary: {self._calculate_salary()}"
        )

    # Setter method (Safe update lever)
    def setBaseSalary(self, new_base_salary):
        Employee._base_salary = new_base_salary


# Test execution
emp1 = Employee("Angela", 10, "Clerk")
emp1.generate_payslip()

emp1.setBaseSalary(70000)
emp2 = Employee("Angela", 4, "Clerk")
emp2.generate_payslip()
```
* **Output:**
  ```text
  Name: Angela 
  Position: Clerk 
  Level: 10 
  Salary: 100000.0
  Name: Angela 
  Position: Clerk 
  Level: 4 
  Salary: 98000.0
  ```

### Drill 2: Inheritance (Person Base Class with Employee & Student Subclasses)
```python
# Base Class
class Person:
    def __init__(self, name, age, gender, ID):
        self.name = name
        self.age = age
        self.gender = gender
        self.ID = ID

    def ID_card(self):
        print(
            f"Identity Number: {self.ID} \nName: {self.name} \nGender: {self.gender} \nAge: {self.age}"
        )


# Subclass 1: Employee
class Employee(Person):
    def __init__(self, name, age, gender, ID, company, portfolio, salary):
        Person.__init__(self, name, age, gender, ID)
        self.company = company
        self.portfolio = portfolio
        self.salary = salary

    def set_salary(self, new_salary):
        self.salary = new_salary


# Subclass 2: Student
class Student(Person):
    def __init__(self, name, age, gender, ID, school, course, level):
        Person.__init__(self, name, age, gender, ID)
        self.school = school
        self.course = course
        self.level = level

    def update_level(self):
        self.level += 100


# Testing Inheritance
emp = Employee("Ola", 45, "Male", "214892", "Rain", "Data Scientist", 20000)
emp.ID_card()  # Inherited from Person without redefining!

stu = Student("Moji", 34, "Female", "213456", "Rain", "AI", 200)
stu.ID_card()  # Inherited from Person!
stu.update_level()
print("Updated Student Level:", stu.level)
```
* **Output:**
  ```text
  Identity Number: 214892 
  Name: Ola 
  Gender: Male 
  Age: 45

  --- Student Details ---
  Identity Number: 213456 
  Name: Moji 
  Gender: Female 
  Age: 34
  Updated Student Level: 300
  ```

---

## 4. Bridge to Data Science & Bioinformatics

* **In Machine Learning Pipelines:** Scikit-Learn's estimators inherit from a base `BaseEstimator` and `ClassifierMixin` or `RegressorMixin`. They encapsulate internal model weights (`model.coef_`, `model.intercept_`) and expose clean public methods (`fit()`, `predict()`).
* **In Bioinformatics Workflows:** We can define a base `BiologicalSequence` class holding universal attributes (`sequence_id`, `length`, `alphabet`) and methods (`gc_content()`). Derived classes like `DNASequence`, `RNASequence`, and `ProteinSequence` can inherit these baseline features while adding specialized methods (e.g., `transcribe()` for DNA, `translate()` for RNA, `compute_isoelectric_point()` for Protein).