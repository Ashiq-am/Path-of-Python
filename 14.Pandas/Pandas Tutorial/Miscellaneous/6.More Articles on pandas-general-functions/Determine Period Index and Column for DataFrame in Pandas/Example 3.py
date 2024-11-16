import pandas as pd

Team = ["Ind", "Pak", "Aus"]

# pass the period and staring index
match_date = pd.period_range('2020-08-01', periods=3)

# Determine Period Index and Column for DataFrame
df = pd.DataFrame(Team, index=match_date, columns=['Team'])

df
