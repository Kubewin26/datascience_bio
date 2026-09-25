# AI / Machine Learning Foundations Program
## Official Curriculum for New Learners

**Program length:** 4 months  
**Class schedule:** 3 sessions per week (~48 sessions total)  
**Session length:** 2–2.5 hours  
**Level:** Absolute beginner — **no prior coding or math degree required**  
**Format:** Live coding classes + homework + quizzes + real projects + final capstone  

This document is your map of the whole program: what you will learn, when you will learn it, what “good” looks like, and how you will be assessed.

---

## 1. Program promise

By the end of this program you will be able to:

1. Write beginner-to-intermediate **Python** for data work  
2. Clean, join, and analyze tables with **NumPy** and **Pandas**  
3. Create clear charts and tell a data story with **Matplotlib / Seaborn**  
4. Build and evaluate **supervised ML models** (regression & classification)  
5. Use **decision trees / Random Forest** and basic **clustering**  
6. Follow a full **ML pipeline** from raw data → model → demo  
7. Present results to a non-technical audience and publish a **portfolio**  

You will **not** be expected to become a research scientist in 4 months. You **will** be expected to become a confident junior practitioner who can complete a real analysis/ML project end to end.

---

## 2. Who this program is for

### Ideal learner
- New to programming  
- Interested in data analysis, AI, or ML careers / upskilling  
- Willing to practice 3–5 hours outside class each week  
- Comfortable learning by doing (typing code, making errors, fixing them)

### Not required before day 1
- Prior coding experience  
- Advanced mathematics  
- Statistics degree  
- Expensive cloud accounts  

### Helpful (but optional)
- Basic computer skills (files, folders, copy/paste, browsers)  
- Curiosity about Excel-style tables and charts  

---

## 3. Tools you will use

| Tool | Purpose |
|------|---------|
| Anaconda / Python | Your programming language and package manager |
| Jupyter Notebook | Where most lessons and homework happen |
| VS Code (optional) | Code editor |
| NumPy | Fast numeric arrays |
| Pandas | Tables / DataFrames |
| Matplotlib & Seaborn | Charts |
| scikit-learn | Machine learning |
| Streamlit | Simple app demo for your model |
| GitHub | Portfolio and project backup |

**Setup notebook:** `00_Setup/Environment_Setup.ipynb`  
**Packages:** install with `pip install -r requirements.txt`

---

## 4. How learning works each week

Each week has **3 sessions**:

| Session | Focus |
|---------|--------|
| **A** | New concept + live coding with the instructor |
| **B** | Guided practice (you code along / complete drills) |
| **C** | Lab, quiz, or mini-project |

### Weekly time expectation
- **In class:** ~6–7.5 hours  
- **Homework:** ~3–5 hours  

### Assessment types
| Type | What it is | Frequency |
|------|------------|-----------|
| Assignments (A1–A8) | Graded homework notebooks | Roughly every 1–2 weeks |
| Quizzes (Q1–Q8) | Short technical checks | Every 2 weeks |
| Real-time projects (RT1–RT6) | In-class collaborative builds | Key milestone weeks |
| Capstone | Final project + presentation | Weeks 14–16 |

---

## 5. Program roadmap (big picture)

```text
Month 1  →  Think like a programmer (Python)
Month 2  →  Work with real tables (NumPy + Pandas)
Month 3  →  See patterns + start ML (Viz + first models)
Month 4  →  Ship real ML work (stronger models + capstone)
```

| Month | Theme | You will leave able to… |
|-------|--------|-------------------------|
| 1 | Python Foundations | Write scripts with variables, decisions, loops, functions, lists/dicts |
| 2 | Data Analysis Toolkit | Load CSVs, clean data, group, merge, answer business questions |
| 3 | Visualization & ML Start | Build EDA charts; prepare data; train first regression/classification models |
| 4 | Applied ML & Capstone | Evaluate models properly; use trees/forest/clustering; present a finished project |

---

## 6. Core skills checklist (everything you need to learn)

Use this as a personal progress list. Check items as you master them.

### A. Computer & workflow
- [ ] Install Anaconda and open Jupyter  
- [ ] Create, rename, save notebooks  
- [ ] Read common errors (`NameError`, `SyntaxError`, `FileNotFoundError`, `ModuleNotFoundError`)  
- [ ] Keep an organized project folder  
- [ ] (Later) Push work to GitHub  

### B. Python programming
- [ ] Variables and data types (`int`, `float`, `str`, `bool`)  
- [ ] Input / print  
- [ ] Operators and expressions  
- [ ] `if / elif / else`  
- [ ] `for` and `while` loops  
- [ ] Strings and string methods  
- [ ] Lists, tuples, sets, dictionaries  
- [ ] Indexing and slicing  
- [ ] Writing and calling functions  
- [ ] `return` values and parameters  
- [ ] Light OOP: class, object, method (intro only)  
- [ ] Writing clean, readable code with comments  

### C. NumPy
- [ ] Create arrays  
- [ ] Shape, dtype, indexing, slicing  
- [ ] Element-wise operations  
- [ ] Basic aggregations (sum, mean, min, max)  
- [ ] Why arrays beat plain lists for numeric work  

### D. Pandas / data wrangling
- [ ] Series vs DataFrame  
- [ ] Read/write CSV  
- [ ] Select columns and filter rows  
- [ ] Handle missing data  
- [ ] Sort, rename, create columns  
- [ ] `groupby` aggregations  
- [ ] Merge / join / concatenate tables  
- [ ] Basic data quality checks  

### E. Visualization & storytelling
- [ ] Choose the right chart for the question  
- [ ] Histograms, bar charts, line charts, scatter plots  
- [ ] Seaborn distributions / categorical plots  
- [ ] Titles, labels, legends  
- [ ] Explain a chart in plain English  

### F. Stats for ML (practical, not theoretical)
- [ ] Mean vs median  
- [ ] Spread (std / variance intuition)  
- [ ] Correlation (and “correlation ≠ causation”)  
- [ ] Train/test split purpose  
- [ ] Overfitting vs underfitting intuition  

### G. Machine learning
- [ ] What AI vs ML means in practice  
- [ ] ML lifecycle / pipeline steps  
- [ ] Supervised vs unsupervised  
- [ ] Data cleaning for ML  
- [ ] Preprocessing: encoding, scaling, imputation  
- [ ] Feature engineering basics  
- [ ] Linear regression  
- [ ] Logistic regression / classification  
- [ ] Decision trees  
- [ ] Random Forest  
- [ ] K-Means clustering  
- [ ] PCA intuition (dimension reduction / visualization)  
- [ ] Evaluation metrics: accuracy, precision, recall, F1, MAE, RMSE, R²  
- [ ] Confusion matrix  
- [ ] Cross-validation idea  
- [ ] Compare at least two models fairly  
- [ ] Responsible AI / bias awareness  
- [ ] Save a model and demo it (Streamlit or live notebook)  

---

## 7. Detailed weekly curriculum

### Legend
- **Learn** = concepts and skills taught  
- **Do** = practice in class / homework  
- **Materials** = files in this repository  

---

### MONTH 1 — Python Foundations (Weeks 1–4)

#### Week 1 — Getting started
**Learning objectives**
- Set up your environment successfully  
- Understand what AI/ML is at a beginner level  
- Write and run your first Python cells  

| Session | Learn | Do |
|---------|-------|----|
| A | Program overview; AI vs ML vs Data Science (simple definitions); Anaconda + Jupyter | Complete setup checklist |
| B | Variables, types, `print`, `input`, basic arithmetic | Type-along drills |
| C | Notebook habits; reading errors | “Hello data” success cell + exit ticket |

**Materials:** `00_Setup/Environment_Setup.ipynb`, `python basic .ipynb`  
**You should be able to:** open Jupyter, run code, save a notebook, explain what a variable is.

---

#### Week 2 — Decisions and loops
**Learning objectives**
- Control program flow with conditions and loops  
- Trace what code will do before running it  

| Session | Learn | Do |
|---------|-------|----|
| A | Boolean logic; `if / elif / else` | Grade / age / eligibility examples |
| B | `for` loops, `while` loops, `range` | Pattern printing + counters |
| C | Mixed drills | **Quiz Q1** |

**Materials:** `python basics/ProgramFlow.ipynb`, `Quizzes/Q1_student.md`  
**You should be able to:** write a small decision program and a loop without copying blindly.

---

#### Week 3 — Data structures
**Learning objectives**
- Store collections of values  
- Access and update list/dict data  

| Session | Learn | Do |
|---------|-------|----|
| A | Strings + lists (indexing, slicing, methods) | String/list exercises |
| B | Dictionaries, tuples, sets | Lookup / membership drills |
| C | Combined practice | **Assignment A1** workshop |

**Materials:** `python basics/Data Structures*.ipynb`, `DataStructure-Strings and Lists.ipynb`, `string.ipynb`, assignment notebooks  
**You should be able to:** build a list of records and look up values in a dictionary.

---

#### Week 4 — Functions and light OOP + mini project
**Learning objectives**
- Package logic into reusable functions  
- Meet classes/objects at intro level  
- Finish a small applied Python project in class  

| Session | Learn | Do |
|---------|-------|----|
| A | Functions, parameters, return values | Function drills |
| B | Classes & objects (intro only) | Simple class examples |
| C | Mini project day | **RT1** (e.g. car insurance / bill logic) + **Quiz Q2** |

**Materials:** `FUNCTIONS*.ipynb`, `CLASSES AND OOP*.ipynb`, `car_insurance.ipynb`, `project.ipynb`  
**Month 1 outcome:** You can write a short Python program that uses functions and collections to solve a real-ish problem.

---

### MONTH 2 — Data Analysis Toolkit (Weeks 5–8)

#### Week 5 — NumPy
**Learning objectives**
- Use arrays for numeric computation  
- Index, slice, and aggregate array data  

| Session | Learn | Do |
|---------|-------|----|
| A | Arrays, dtypes, shape | Create and inspect arrays |
| B | Indexing, slicing, operations | Vectorized calculations |
| C | Practice lab | **Assignment A3** |

**Materials:** `NumPy/*.ipynb`  
**You should be able to:** compute means/sums on arrays and explain shape.

---

#### Week 6 — Pandas foundations
**Learning objectives**
- Work with Series and DataFrames  
- Select, filter, and inspect tabular data  

| Session | Learn | Do |
|---------|-------|----|
| A | Series, DataFrames, basic inspection | `head`, `info`, `describe` |
| B | Selection, filters, missing values | Cleaning starter drills |
| C | Consolidation | **Quiz Q3** (NumPy check) + Pandas practice |

**Materials:** `Pandas/Introduction to Pandas.ipynb`, `Series.ipynb`, `DataFrames.ipynb`, `Missing Data.ipynb`  
**You should be able to:** load a mental model of rows/columns and filter a table.

---

#### Week 7 — Grouping and combining data
**Learning objectives**
- Answer “by category” questions with `groupby`  
- Combine multiple tables  

| Session | Learn | Do |
|---------|-------|----|
| A | `groupby` + aggregations | Summaries by category |
| B | Merge / join / concat | Key-based combines |
| C | Applied exercise | **Assignment A4** (SF Salaries part) |

**Materials:** `Groupby.ipynb`, `Merging, Joining, and Concatenating .ipynb`, `Pandas Exercises/SF Salaries Exercise.ipynb`  
**You should be able to:** compute group averages and merge two CSVs on a key.

---

#### Week 8 — Pandas project week
**Learning objectives**
- Use Pandas end-to-end on a realistic dataset  
- Start thinking like an analyst  

| Session | Learn | Do |
|---------|-------|----|
| A | CSV I/O + Pandas operations | File workflows |
| B | Ecommerce Purchases exercise | Business questions in code |
| C | Live team analysis | **RT2 Arise project** + **Quiz Q4** |

**Materials:** `Data Input and Output.ipynb`, `Operations.ipynb`, Ecommerce exercise, `pandas_project/`  
**Optional start:** `Portfolio/github_portfolio_guide.ipynb`  
**Month 2 outcome:** You can take a CSV, clean it, analyze it, and answer questions with evidence.

---

### MONTH 3 — Visualization & Machine Learning Start (Weeks 9–12)

#### Week 9 — Matplotlib foundations
**Learning objectives**
- Create standard charts  
- Match chart type to the question  

| Session | Learn | Do |
|---------|-------|----|
| A | Matplotlib basics (line, bar, scatter) | Reproduce charts |
| B | Distributions & categorical plots | Histogram / bar practice |
| C | Chart critique | Fix misleading charts; start **A5** |

**Materials:** Teclov Matplotlib notebooks, `Matplotlib Concepts Lecture.ipynb`, exercises  
**You should be able to:** plot a clean labeled chart from a DataFrame column.

---

#### Week 10 — Seaborn, storytelling, civic data lab
**Learning objectives**
- Build richer EDA visuals  
- Join real public datasets and present findings  

| Session | Learn | Do |
|---------|-------|----|
| A | Seaborn + Pandas built-in viz | Distribution / categorical / heat-style plots |
| B | Time series / multi-plot stories | Narrative practice |
| C | Applied lab | **RT3 Boston 311** join & plot + **Quiz Q5** |

**Materials:** `Datavisual/.../Seaborn/*`, time-series notebook, `boston_*.csv`  
**You should be able to:** produce a 3–5 chart mini-story with written insights.

---

#### Week 11 — Stats for ML + data preparation
**Learning objectives**
- Use practical stats to prepare for modeling  
- Clean and preprocess data the ML way  

| Session | Learn | Do |
|---------|-------|----|
| A | Mean/median, spread, correlation, train/test, overfitting intuition; ML lifecycle | Stats notebook walkthrough |
| B | Data cleaning for ML | Titanic/housing cleaning |
| C | Preprocessing lab | Scaling/encoding + **Assignment A6** |

**Materials:**  
- `Stats_for_ML/stats_for_ml.ipynb`  
- `ML/Introduction_ML/intro.ipynb`  
- `ML/Introduction_ML/mllifecylcle.ipynb`  
- `data_cleaning.ipynb`, `data_preprocessing.ipynb`, `feature_engineering.ipynb`  

**You should be able to:** explain train/test split and prepare a clean feature table.

---

#### Week 12 — First supervised models
**Learning objectives**
- Train linear regression and logistic classification  
- Interpret simple model outputs  

| Session | Learn | Do |
|---------|-------|----|
| A | Linear regression | Fit + predict continuous targets |
| B | Classification / logistic regression | Binary classification practice |
| C | Baseline project | **RT4 Titanic baseline** + **Quiz Q6** |

**Materials:** `linear_regression.ipynb`, `classification.ipynb`, `supervised_ML.ipynb`, Titanic CSV  
**Month 3 outcome:** You can run a first ML experiment and explain what the model is trying to predict.

---

### MONTH 4 — Applied ML & Capstone (Weeks 13–16)

#### Week 13 — Evaluation and stronger models
**Learning objectives**
- Judge models with the right metrics  
- Use trees and Random Forest  

| Session | Learn | Do |
|---------|-------|----|
| A | Accuracy, precision, recall, F1, MAE/RMSE/R², confusion matrix, CV | Metrics lab |
| B | Decision trees | Visualize a simple tree |
| C | Random Forest comparison lab | **A7/A8** progress |

**Materials:**  
- `ML/evaluation/model_evaluation.ipynb`  
- `ML/trees_ensembles/decision_trees_random_forest.ipynb`  
- `Assignments_A6_A8.md`  

**You should be able to:** compare two models and defend which is better for the business risk.

---

#### Week 14 — Unsupervised learning + capstone kickoff
**Learning objectives**
- Cluster unlabeled data  
- Reduce dimensions with PCA intuition  
- Choose and start your capstone  

| Session | Learn | Do |
|---------|-------|----|
| A | K-Means + PCA | Segment + 2D visualization |
| B | Promotion case workshop | **RT5** |
| C | Capstone launch | Pick Track A/B/C + **Quiz Q7** |

**Materials:**  
- `ML/unsupervised/kmeans_pca.ipynb`  
- `ML/pipeline/end_to_end_ml_pipeline.ipynb`  
- `Capstone/` + `project/promotion_dataset.csv`  

**You should be able to:** state your capstone problem, dataset, and success metric.

---

#### Week 15 — Responsible AI + demo packaging
**Learning objectives**
- Spot bias and communicate limitations  
- Package a simple demo for stakeholders  

| Session | Learn | Do |
|---------|-------|----|
| A | Bias sources; metric fairness; human oversight | Ethics discussion + exit ticket |
| B | Streamlit demo | Wire inputs → prediction |
| C | Capstone build lab | Modeling + README progress |

**Materials:** `ML/ethics/responsible_ai_bias.ipynb`, `Deploy/streamlit_demo_guide.ipynb`, `Deploy/app.py`  
**You should be able to:** run a local demo and write one bias/limitation paragraph.

---

#### Week 16 — Capstone clinic, present, close
**Learning objectives**
- Finish, present, and portfolio-package your work  
- Defend your pipeline in a short technical oral/quiz  

| Session | Learn | Do |
|---------|-------|----|
| A | Debugging clinic / peer help | Fix blockers |
| B | Presentations + peer review | 8–10 min talks |
| C | Close-out | **Quiz Q8** + portfolio checklist |

**Materials:** `Capstone/RUBRIC.md`, `Portfolio/github_portfolio_guide.ipynb`, `Quizzes/Q8_student.md`  
**Month 4 outcome:** You have a completed project you can show an employer or school panel.

---

## 8. Capstone (final project)

Full briefs live in `Capstone/`.

### Choose one track
| Track | Project | Main data |
|-------|---------|-----------|
| **A** | HR Promotion Predictor | `project/promotion_dataset.csv` |
| **B** | Credit Risk Scoring | `project/german_credit/german_credit_data.csv` |
| **C** | Civic Ops Analytics (Boston) | `boston_311_calls.csv` + related CSVs |

### Required deliverables
1. Clean analysis + modeling notebook(s)  
2. README explaining problem, approach, results, limitations  
3. Model comparison with proper metrics  
4. Demo (Streamlit **or** live notebook walkthrough)  
5. 8–10 minute presentation  
6. Ethics / limitations reflection  

### Rubric (100 points)
- Data quality & EDA — 25  
- Modeling & evaluation — 30  
- Code clarity — 15  
- Demo & presentation — 20  
- Insight & responsibility — 10  

Details: `Capstone/RUBRIC.md`

---

## 9. Assignments and quizzes at a glance

### Assignments
| ID | Week | Focus |
|----|------|-------|
| A1 | 3 | Python drills (grades/lists/dicts) |
| A2 | 4 | Functions / light applied logic |
| A3 | 5 | NumPy lab |
| A4 | 7–8 | Pandas salaries + ecommerce |
| A5 | 9–10 | Visualization story |
| A6 | 11 | Cleaning + feature engineering |
| A7 | 12–13 | Regression report |
| A8 | 13–14 | Classification report |

### Quizzes
| Quiz | Week | Focus |
|------|------|-------|
| Q1 | 2 | Variables, if/else, loops |
| Q2 | 4 | Functions, lists/dicts, errors |
| Q3 | 6 | NumPy |
| Q4 | 8 | Pandas |
| Q5 | 10 | Charts / EDA thinking |
| Q6 | 12 | ML foundations |
| Q7 | 14 | Metrics, trees, clustering |
| Q8 | 16 | Capstone defense |

Student sheets: `Quizzes/Qn_student.md` (answer keys are facilitator-only).

---

## 10. Optional stretch topics

If the class is moving well, facilitators may add:
- Light **SQL** (`00_Setup/SQL_Basics_Optional.md`)  
- Extra Plotly / geo plotting  
- Deeper feature engineering  
- Intro neural nets / NLP (**not required** for graduation)

These are enrichment, not core graduation requirements.

---

## 11. What “done” looks like for a graduate

A successful graduate can:
- Open a new CSV and perform EDA without panicking  
- Clean missing values and document decisions  
- Train and evaluate at least two models  
- Explain precision vs recall in plain language  
- Present charts and model results to a non-technical listener  
- Show a GitHub (or shared) portfolio with homework + capstone  

### Portfolio minimum
- 2 homework notebooks  
- 1 visualization/EDA project  
- Capstone folder with README  
- Short skills list  

Guide: `Portfolio/github_portfolio_guide.ipynb`

---

## 12. Beginner success habits

1. **Type the code** — do not only watch  
2. **Run cells in order** — many errors are “you skipped a cell”  
3. **Read the error’s last line first**  
4. **Keep a mistakes notebook** — write the error + the fix  
5. **Ask specific questions** (“line 12 NameError on `df`”) not only “it doesn’t work”  
6. **Practice a little every day** better than one long cram  
7. **Explain aloud** what your chart/model means  

---

## 13. Glossary (first-pass definitions)

| Term | Simple meaning |
|------|----------------|
| **Variable** | A named box that stores a value |
| **Function** | A reusable block of code that does one job |
| **DataFrame** | A spreadsheet-like table in Pandas |
| **Feature (X)** | Input columns used to predict |
| **Target (y)** | The column you want to predict |
| **Train/test split** | Hide some data to check real performance |
| **Overfitting** | Memorizing training data; fails on new data |
| **Classification** | Predict a category (spam/not, promote/not) |
| **Regression** | Predict a number (price, score) |
| **Metric** | A score that says how good predictions are |
| **Pipeline** | Ordered steps from raw data to model |
| **Bias (ethics)** | Systematic unfairness against a group |

---

## 14. Repository guide (where to click)

```text
GET_Analysis/
├── CURRICULUM.md                 ← facilitator working map
├── PROGRAM_CURRICULUM.md         ← this learner curriculum
├── requirements.txt
├── 00_Setup/                     ← install & optional SQL
├── python basics/                ← Month 1
├── NumPy/                        ← Week 5
├── Pandas/                       ← Weeks 6–8
├── Datavisual/                   ← Weeks 9–10
├── Stats_for_ML/                 ← Week 11
├── ML/                           ← Weeks 11–15
├── Deploy/                       ← Streamlit demo
├── Portfolio/                    ← GitHub guide
├── Quizzes/                      ← Q1–Q8
├── Capstone/                     ← final project briefs
├── Assignments_A6_A8.md
└── project/ + datasets           ← capstone / labs data
```

---

## 15. Opening message to learners

Welcome. You do not need to be “good at computers” on day one. You need consistency.

If you show up, type the code, submit the practice, and ask questions when stuck, you can finish this program with a real project and a portfolio that proves your skills.

**Start here today:** open `00_Setup/Environment_Setup.ipynb` and get your SUCCESS message.

---

*Curriculum version: aligned to GET_Analysis materials · 16-week beginner AI/ML path*
