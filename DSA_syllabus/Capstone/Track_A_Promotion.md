# Track A — HR Promotion Predictor

## Business problem
An organization wants to understand which employees are likely to be **promoted** and which factors matter — without blindly trusting a black-box score.

## Dataset
- `project/promotion_dataset.csv`
- Brief: `project/GET CASE STUDY.docx`

## Required technical work
1. Load + inspect schema; write a mini data dictionary (column → meaning)
2. Clean missing values / duplicates; document decisions
3. EDA: class balance, key group comparisons, 4–6 charts
4. Preprocess (impute, encode, scale as needed) inside a Pipeline if possible
5. Train **at least two** classifiers (e.g. Logistic Regression + Random Forest)
6. Compare with the **same** metric set (accuracy, precision, recall, F1, confusion matrix)
7. Interpret: top features / coefficients / importances + business language
8. Optional stretch: Streamlit form for a single employee profile

## Suggested questions to answer
- How balanced is promotion vs not?
- Which departments / education levels differ most?
- What errors is the model most likely to make?
- Should HR use this as automation or decision support?

## Demo script (2 minutes)
1. Show one EDA chart
2. Show confusion matrix
3. Predict for one sample employee
4. State one limitation
