# AI/ML Beginner Course — Facilitator Working Map

> **Learners:** use the full program curriculum here → [`PROGRAM_CURRICULUM.md`](PROGRAM_CURRICULUM.md)  
> This file is the short facilitator map (paths, assessments, weekly A/B/C).

**Duration:** 4 months · **Pace:** 3 sessions/week · **~48 sessions**  
**Audience:** Absolute beginners (no prior coding)  
**Session length:** 2–2.5 hours  
**Pattern:** A = teach + live code · B = guided practice · C = project lab / quiz / review  
**Install:** `pip install -r requirements.txt` (after Anaconda setup)

---

## Materials map

| Module | Status | Path |
|--------|--------|------|
| Environment setup | Ready | `00_Setup/Environment_Setup.ipynb` |
| Optional SQL stretch | Ready | `00_Setup/SQL_Basics_Optional.md` |
| Python basics | Ready | `python basics/` |
| NumPy | Ready | `NumPy/` |
| Pandas | Ready | `Pandas/`, `Pandas Exercises/`, `pandas_project/` |
| Visualization | Ready | `Datavisual/` |
| Stats for ML | Ready | `Stats_for_ML/stats_for_ml.ipynb` |
| ML intro + cleaning | Ready | `ML/Introduction_ML/`, `ML/data_cleaningML/` |
| Model evaluation | Ready | `ML/evaluation/model_evaluation.ipynb` |
| Trees + Random Forest | Ready | `ML/trees_ensembles/decision_trees_random_forest.ipynb` |
| K-Means + PCA | Ready | `ML/unsupervised/kmeans_pca.ipynb` |
| End-to-end pipeline | Ready | `ML/pipeline/end_to_end_ml_pipeline.ipynb` |
| Ethics / bias | Ready | `ML/ethics/responsible_ai_bias.ipynb` |
| Streamlit demo | Ready | `Deploy/streamlit_demo_guide.ipynb`, `Deploy/app.py` |
| GitHub portfolio | Ready | `Portfolio/github_portfolio_guide.ipynb` |
| Quizzes Q1–Q8 | Ready | `Quizzes/` |
| Capstone A/B/C + rubric | Ready | `Capstone/` |
| Assignments A6–A8 | Ready | `Assignments_A6_A8.md` |
| Projects / datasets | Ready | `project/`, Boston CSVs, Titanic, heart, diabetes |

---

## 4-month plan

| Month | Theme | Weeks | Outcome |
|-------|--------|-------|---------|
| 1 | Python foundations | 1–4 | Control flow, functions, lists/dicts; mini project |
| 2 | Data analysis toolkit | 5–8 | NumPy + Pandas; merge/clean/group; Arise-style analysis |
| 3 | Visualization + ML foundations | 9–12 | EDA dashboards; stats; preprocessing; first supervised models |
| 4 | Applied ML + capstone | 13–16 | Trees/ensembles, clustering, evaluation; ship + demo |

---

## Assessments

### Assignments
| ID | When | Task | Materials |
|----|------|------|-----------|
| A1 | Wk 3 | Grade calculator + list/dict drills | `python basics/assign`, `grade`, `assig1` |
| A2 | Wk 4 | Functions + light OOP | `FUNCTIONS`, `car_insurance` |
| A3 | Wk 5 | NumPy array lab | `NumPy/Numpy Exercise` |
| A4 | Wk 7–8 | SF Salaries + Ecommerce | `Pandas/Pandas Exercises/` |
| A5 | Wk 9–10 | Viz story (sales or crypto) | `Datavisual/` datasets |
| A6 | Wk 11 | Cleaning + feature engineering | `Assignments_A6_A8.md` |
| A7 | Wk 12–13 | Regression report | `Assignments_A6_A8.md` |
| A8 | Wk 13–14 | Classification report | `Assignments_A6_A8.md` |

### Real-time class projects
| ID | Week | Project |
|----|------|---------|
| RT1 | 4 | Car insurance / bill mini-app |
| RT2 | 8 | Arise / application_data live analysis |
| RT3 | 10 | Boston 311 + population join & plot |
| RT4 | 12 | Titanic EDA → baseline logistic regression |
| RT5 | 14 | Promotion prediction (GET case study) |
| RT6 | 16 | Capstone clinic + peer review |

### Technical quizzes
Student sheets + answer keys in `Quizzes/` (`Q1_student.md` … `Q8_answers.md`).

---

## Capstone (Weeks 14–16)

See `Capstone/README.md`.

- **Track A** — HR Promotion (`Track_A_Promotion.md`)
- **Track B** — Credit Risk (`Track_B_Credit_Risk.md`)
- **Track C** — Civic Boston (`Track_C_Civic_Boston.md`)
- **Rubric** — `Capstone/RUBRIC.md`

---

## Weekly curriculum

### Month 1 — Python foundations

| Week | Session A | Session B | Session C | Materials |
|------|-----------|-----------|-----------|-----------|
| 1 | What is AI/ML + install tooling | Variables, types, input/print | First notebook lab + error reading | `00_Setup/Environment_Setup.ipynb`, `python basic .ipynb` |
| 2 | Conditionals & program flow | Loops (for/while) | **Q1** | `ProgramFlow.ipynb`, `Quizzes/Q1_*` |
| 3 | Strings & lists | Dicts, tuples, sets | **A1** workshop | Data Structures notebooks |
| 4 | Functions | Intro OOP (light) | **RT1** + **Q2** | `FUNCTIONS*`, `CLASSES AND OOP*`, `car_insurance` |

### Month 2 — NumPy & Pandas

| Week | Session A | Session B | Session C | Materials |
|------|-----------|-----------|-----------|-----------|
| 5 | NumPy arrays & dtypes | Indexing, slicing, ops | **A3** | `NumPy/*.ipynb` |
| 6 | Pandas Series & DataFrames | Selection, filters, missing data | **Q3** | Intro, Series, DataFrames, Missing Data |
| 7 | Groupby & aggregations | Merge / join / concat | **A4** SF Salaries | Groupby, Merging, SF Salaries |
| 8 | CSV I/O + Operations | Ecommerce Purchases | **RT2** Arise + **Q4** | Data I/O, Ecommerce, `pandas_project/` · optional: start `Portfolio/github_portfolio_guide.ipynb` |

### Month 3 — Visualization & ML start

| Week | Session A | Session B | Session C | Materials |
|------|-----------|-----------|-----------|-----------|
| 9 | Matplotlib fundamentals | Distributions & categorical plots | Chart critique lab | Teclov + Matplotlib lecture/exercises |
| 10 | Seaborn + Pandas viz | Time-series / multi-plot stories | **RT3** Boston 311 + **Q5** | Seaborn/*, Boston CSVs |
| 11 | Stats for ML + ML lifecycle | Data cleaning for ML | Preprocessing + scaling (**A6**) | `Stats_for_ML/stats_for_ml.ipynb`, `intro`, `mllifecylcle`, cleaning, preprocessing, feature_engineering |
| 12 | Linear regression | Classification (logistic) | **RT4** Titanic + **Q6** | `linear_regression`, `classification`, Titanic |

### Month 4 — Applied ML & capstone

| Week | Session A | Session B | Session C | Materials |
|------|-----------|-----------|-----------|-----------|
| 13 | Evaluation metrics + CV | Decision trees | Random Forest lab (**A7/A8**) | `ML/evaluation/model_evaluation.ipynb`, `ML/trees_ensembles/decision_trees_random_forest.ipynb` |
| 14 | K-Means + PCA | **RT5** Promotion workshop | **Q7** + capstone kickoff | `ML/unsupervised/kmeans_pca.ipynb`, `Capstone/`, `ML/pipeline/end_to_end_ml_pipeline.ipynb` |
| 15 | Responsible AI / bias | Streamlit demo packaging | Capstone build lab | `ML/ethics/responsible_ai_bias.ipynb`, `Deploy/` |
| 16 | Capstone clinic | Presentations + peer review | **Q8** + portfolio checklist | `Capstone/RUBRIC.md`, `Portfolio/`, `Quizzes/Q8_*` |

---

## Facilitator notes

- Prefer one official notebook per beginner topic; archive duplicates.
- Do not rush Month 1 — functions must feel comfortable before Pandas.
- Homework: 3–5 hours/week.
- Pairs for real-time projects; quizzes individual; capstone solo or pair.
- Demo app: `streamlit run Deploy/app.py`

## Session time box

| Block | Minutes |
|-------|---------|
| Concept / why it matters | 20 |
| Live coding | 50–70 |
| Student practice | 30–40 |
| Exit ticket / wrap | 10 |
