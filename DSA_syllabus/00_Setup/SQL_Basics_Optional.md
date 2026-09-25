# Optional — SQL Basics for Analysts (1 week stretch)

Use this if your cohort aims at analyst roles. Insert as a flex week after Pandas (between Week 8 and 9) **or** as bonus homework.

## Learning goals
- SELECT, WHERE, ORDER BY
- aggregations: COUNT, SUM, AVG, GROUP BY
- JOIN intuition (matches Pandas merge)

## Suggested free labs
- Mode SQL tutorial / W3Schools SQL / SQLBolt
- Practice: recreate a Pandas groupby using SQL on the same CSV loaded into SQLite

## Mini SQLite lab (Python)

```python
import pandas as pd
import sqlite3

df = pd.read_csv("../Pandas/Pandas Exercises/Salaries.csv")
con = sqlite3.connect(":memory:")
df.to_sql("salaries", con, index=False)

query = """
SELECT JobTitle, AVG(TotalPay) AS avg_pay, COUNT(*) AS n
FROM salaries
GROUP BY JobTitle
ORDER BY avg_pay DESC
LIMIT 10;
"""
print(pd.read_sql_query(query, con))
```

## Exit criteria
Student can write a query with filter + group + order and explain how it maps to Pandas.
