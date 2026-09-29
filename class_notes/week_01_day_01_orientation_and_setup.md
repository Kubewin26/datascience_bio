# Week 1, Day 1: Course Orientation & Professional Workstation Setup

**Course:** Data Science & Machine Learning (Incubator Hub - DSA 2.0)  
**Instructor:** Israel Odeajo  
**Student:** Winner Kubeyinje (`hswkbioinfo`)  

---

## 1. What is Machine Learning? (The Big Paradigm Shift)

In traditional programming, humans write all the rules:
* **Traditional Coding:** $\text{Data} + \text{Rules} = \text{Answers}$  
  *Example:* A human writes an `if/else` rule: *"If a patient's fasting glucose is 126 or higher, flag them as diabetic."*

In Machine Learning, we flip this around:
* **Machine Learning:** $\text{Data} + \text{Answers} = \text{Rules (The Model)}$  
  *Example:* We give the computer 10,000 patient records along with their final diagnoses. The algorithm figures out the complex mathematical patterns on its own and creates a predictive model.

---

## 2. The 4 Roles in the Data Science & AI Industry

In class, we discussed the four primary career paths:

1. **Data Analyst:** Looks at past data to explain what happened (uses SQL, Excel, Power BI, Pandas).
2. **Data Engineer:** Builds the plumbing, databases, and pipelines that transport massive amounts of data safely.
3. **Machine Learning Engineer:** Takes clean data, designs algorithms, and trains models to predict future outcomes.
4. **AI Systems Engineer:** Packages the trained models into fast, secure web apps and APIs that doctors, banks, or customers can actually use.

---

## 3. The 3 Types of Data in Modern AI

1. **Structured Data (Tables):**  
   Data that lives in neat rows and columns like an Excel sheet (e.g., patient ID, age, blood pressure, test scores).
2. **Unstructured Data (Raw Reality):**  
   Data from the real world that doesn't fit into tables (e.g., doctor's handwritten notes, X-ray images, voice recordings, raw DNA sequence files).
3. **Vectors & Embeddings (The AI Bridge):**  
   Computers can't read words or see pictures—they only understand numbers. An **embedding** turns a piece of text or an image into a long list of numbers (coordinates) so the computer can measure how similar two things are.

---

## 4. The 80/20 Rule in Data Science

Israel Odeajo emphasized:
* **80% of our effort** as data scientists goes into data hygiene: finding errors, handling missing numbers, and making sure the data is clean.
* **Only 20% of our effort** is spent training machine learning models.
* *Why?* If you train a model on dirty, corrupted data, your model will give wrong, dangerous predictions ("Garbage In, Garbage Out").

---

## 5. The 4 Practical Hands-on Tasks We Completed on Day 1

On Day 1, we set up a professional, industry-standard development environment using WSL 2 (Ubuntu Linux) and VS Code instead of heavy beginner GUIs like Anaconda Navigator.

### Task 1: Setting up Python & Our Isolated Environment (`ds_env`)
* We verified **Python 3.12** inside Ubuntu WSL.
* We created a clean virtual environment called `ds_env`:
  ```bash
  python3 -m venv ds_env
  source ds_env/bin/activate
  ```
* *Why?* A virtual environment is like giving this project its own private room so its tools never conflict with other projects.
* We installed the core Data Science stack:
  * `numpy` (fast numerical arrays)
  * `pandas` (tables and spreadsheets)
  * `matplotlib` & `seaborn` (charts and data visualization)
  * `scikit-learn` (machine learning models)
  * `pydantic` (data validation)
  * `ipykernel` (lets VS Code run Jupyter Notebooks)
* We registered our custom Jupyter kernel named **`Python (Bio-DS)`**.

### Task 2: Git Version Control & GitHub SSH Security
* We initialized Git on branch `main`.
* We added a `.gitignore` file with `ds_env/` so our heavy virtual environment is never uploaded to GitHub.
* We generated a secure SSH key (`id_ed25519`) and connected it to GitHub (`Kubewin26/datascience_bio.git`).
* *Why?* SSH allows us to push code securely without typing our password every time.

### Task 3: Configuring VS Code with Ruff (Format-on-Save)
* We installed the **Ruff** extension (an ultra-fast Python linter and formatter).
* We configured `.vscode/settings.json` so that whenever we press `Ctrl + S`, Ruff automatically cleans up our Python code style.
* *Important Note:* We scoped this strictly to the **Workspace**, ensuring Prettier (used for web development) remains untouched.

### Task 4: Our First Python Script & Schema Validation (`inspect_schema.py`)
* To practice defensive programming, we created a sample data file: `data/patient_biopsy.json`.
* We wrote a Python script: `scripts/inspect_schema.py` using **Pydantic**:
  ```python
  from pydantic import BaseModel, Field


  class PatientBiopsy(BaseModel):
      patient_id: str
      age: int = Field(ge=0, le=120)  # Age must be between 0 and 120
      tumor_diameter_mm: float = Field(gt=0.0)  # Must be a positive number
      brca1_positive: bool  # Must be True or False
  ```
* *Why?* This script acts like a bouncer at a hospital lab door: if any incoming data has a negative age or a string where a number belongs, it catches the error immediately before it can ruin our data pipeline.

---

## 6. Daily Terminal Commands Cheatsheet

| Command | Plain English Meaning |
| :--- | :--- |
| `cd ~/datascience_bio` | Navigate to our project folder. |
| `source ds_env/bin/activate` | Turn on our project's isolated Python environment. |
| `deactivate` | Turn off the virtual environment. |
| `code .` | Open the current project inside VS Code. |
| `ls -d */` | Show only the folders in the current directory. |
| `git status` | Check which files have been modified or staged. |
| `git add <file>` | Stage a file to be saved in Git. |
| `git commit -m "message"` | Save a permanent snapshot of changes with a description. |
| `git push` | Upload our local Git commits safely to GitHub. |