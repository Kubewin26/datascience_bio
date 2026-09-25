# Track B — Credit Risk Scoring

## Business problem
A lender wants a transparent starter model to flag **higher-risk** credit applicants and explain drivers to a risk manager.

## Dataset
- `project/german_credit/german_credit_data.csv`

## Required technical work
1. Load data; identify target / risk-related columns (document assumptions)
2. Clean + encode categoricals; watch for leakage
3. EDA: risk rate by age, housing, job, credit amount bands
4. Feature engineering (at least 2 new features, e.g. amount bins, age bands)
5. Compare Logistic Regression vs Random Forest (or Tree)
6. Report metrics + confusion matrix; discuss false positives vs false negatives for lending
7. Fairness note: which groups might be harmed by errors? (Week 15 ethics lens)
8. Optional: cluster applicants (K-Means) for segments, then model within/overall

## Suggested questions to answer
- What is the cost of approving a risky applicant vs rejecting a good one?
- Which features dominate the model?
- Is accuracy enough on an imbalanced target?

## Demo script (2 minutes)
1. Risk rate chart by one segment
2. Model comparison table
3. One applicant prediction + explanation
4. Ethics / limitation slide
