# Track C — Civic Ops Analytics (Boston)

## Business problem
A city ops team wants to understand **311 service demand** patterns and whether simple models/rules can help staffing or triage.

## Datasets
- `boston_311_calls.csv`
- `boston_population_by_zip.csv`
- `boston_02128_garbage_schedule.csv`

## Required technical work
1. Load all tables; profile shapes, dates, zip/neighborhood keys
2. Clean + **join/merge** population (and garbage schedule where relevant)
3. EDA: top request types, busy days/hours, per-capita rates by zip
4. Build either:
   - **Analytics track:** executive dashboard (6–10 charts) + actionable recommendations, **or**
   - **ML track:** classify high-volume request types / predict volume band
5. If ML: baseline + stronger model, clear metrics
6. Document data limitations (missing zips, open-text noise, time range)
7. Optional Streamlit: filter by zip/type and show counts

## Suggested questions to answer
- Which request types dominate?
- Do busier areas simply have more people (per-capita view)?
- What should ops do Monday morning differently?

## Demo script (2 minutes)
1. One map-or-bar of demand
2. Per-capita insight
3. Recommendation for ops
4. Data caveat
