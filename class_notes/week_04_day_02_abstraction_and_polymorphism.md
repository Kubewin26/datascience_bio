# Week 4, Day 2: Abstraction, Polymorphism & Real-World OOP Architecture

**Course:** Data Science & Machine Learning (Incubator Hub - DSA 2.0)  
**Instructor:** Israel Odeajo  
**Student:** Winner Kubeyinje (`hswkbioinfo`)  

---

## 1. What I Learned Today (My Personal Reflection)

Today, we wrapped up the four main pillars of Object-Oriented Programming (OOP) by tackling the last two: **Abstraction** and **Polymorphism**, and seeing how they connect in a real-world shopping cart system.

When these concepts were first introduced in class, they sounded like heavy, confusing programming grammar. But breaking them down with simple, everyday pictures made everything clear:

1. **Abstraction is like the light switch on my wall:**
   When I enter my room and flip the plastic switch, the light turns on. I don't need to know what kind of copper wires are inside the wall, the voltage coming from the transformer, or the chemical physics inside the bulb. The messy internal details are hidden from me; I am only given a simple switch to use.
   In Python, an **Abstract Class** is like an empty company rulebook: it says every employee *must* have a way to calculate their payment (`calculate_payment`), but it leaves the actual formula empty. Why? Because part-time staff get paid by the hour, while full-time staff get paid by salary level. Python will refuse to let you create a worker if their specific department doesn't provide that formula.

2. **Polymorphism is like the phrase "Turn Right":**
   Whether you are driving a car, riding a bicycle, or steering a boat, the command is the exact same English phrase: "Turn Right". But a car turns by spinning a wheel, a bicycle turns by leaning handlebars, and a boat turns by moving a rudder. 
   In Python, different classes can have methods with the **exact same name** (like `loan_repayment`), but each class runs its own unique math (compound interest for a commercial bank like UBA vs. a fixed service fee for a non-interest bank like Jaiz). That is method overriding.

3. **Software is built by connecting classes together:**
   The shopping cart exercise showed that real programs don't just sit in one big block. You have an item (`Product`), a container to hold them (`ShoppingCart`), and a checkout system (`Order`). They pass data back and forth using lists and dictionaries.

---

## 2. Code Drills & How They Work

All three drills were tested and confirmed working inside `notebooks/02_functions_practice_lab.ipynb`:

### Drill 1: Abstraction (Enforcing Payment Rules)
```python
from abc import ABC, abstractmethod


# The rulebook: Staff class cannot be created directly
class Staff(ABC):
    def __init__(self, name, job_title, staff_id):
        self.name = name
        self.job_title = job_title
        self.staff_id = staff_id

    def ID_Card(self):
        print(
            f"Staff ID: {self.staff_id} \nName: {self.name} \nPosition: {self.job_title}"
        )

    # Every child class MUST fill this in!
    @abstractmethod
    def calculate_payment(self):
        pass


# Part-time worker fills in their hourly formula
class PT_Staff(Staff):
    def __init__(self, name, job_title, staff_id, hours_of_work):
        super().__init__(name, job_title, staff_id)
        self.hours_of_work = hours_of_work

    def calculate_payment(self):
        return f"{self.hours_of_work * 500:.2f}"


# Full-time worker fills in their level-based formula
class FT_Staff(Staff):
    def __init__(self, name, job_title, staff_id, level):
        super().__init__(name, job_title, staff_id)
        self.level = level

    def calculate_payment(self):
        base_pay = 50000
        amount = ((self.level / 10) * base_pay) + base_pay
        return f"{amount:.2f}"


pt = PT_Staff("Joshua", "Data Scientist", "111", 8)
ft = FT_Staff("Joshua", "Data Scientist", "111", 8)

print("Part-Time Payment: #", pt.calculate_payment())
print("Full-Time Payment: #", ft.calculate_payment())
```
* **Output:**
  ```text
  Part-Time Payment: # 4000.00
  Full-Time Payment: # 90000.00
  ```

### Drill 2: Polymorphism (Same Method Name, Different Calculations)
```python
# Commercial bank uses compound interest
class Bank:
    def __init__(self, bank_name, establishment_year):
        self.bank_name = bank_name
        self.establishment_year = establishment_year

    def loan_repayment(self, amount, number_of_years, interest_rate):
        repayment = amount + (amount * (interest_rate / 100) * number_of_years)
        return f"{repayment:.2f}"


# Non-interest bank overrides with fixed service fee
class NON_Interest_Bank(Bank):
    def loan_repayment(self, amount, number_of_years, service_charge):
        repayment = amount + (service_charge * number_of_years)
        return f"{repayment:.2f}"


uba = Bank("UBA", 1906)
jaiz = NON_Interest_Bank("Jaiz", 2000)

print(f"Commercial Bank: #{uba.loan_repayment(5000000.5504, 5, 4.2)}")
print(f"Non-Interest Bank: #{jaiz.loan_repayment(500000, 3, 5000)}")
```
* **Output:**
  ```text
  Commercial Bank: #6050000.67
  Non-Interest Bank: #515000.00
  ```

### Drill 3: The Shopping Cart Case Study
* Built 3 classes: `Product` (stores item name and price), `ShoppingCart` (holds items in a list `[]`, lets user add, remove, and calculate total), and `Order` (takes the cart and finalizes the checkout).
* Successfully simulated adding laptops and phones, removing the laptop, and printing the finalized order for `$500`.

---

## 3. Why This Matters for My Data Science & Bioinformatics Journey

* **In Machine Learning (Scikit-Learn):** Every model in Scikit-Learn uses polymorphism. Whether you are using Linear Regression, Decision Trees, or Random Forests, they all use the exact same method names: `model.fit(X, y)` to train and `model.predict(X)` to make predictions. I don't have to learn a new verb for every single algorithm.
* **In Bioinformatics Pipelines:** I can create a base `SequenceParser` class with an abstract method `parse()`. Then, whether I am writing a parser for FASTA files, FASTQ files, or GenBank files, each file format implements its own parsing logic under the hood, but my main analysis script just calls `.parse()` on any file!