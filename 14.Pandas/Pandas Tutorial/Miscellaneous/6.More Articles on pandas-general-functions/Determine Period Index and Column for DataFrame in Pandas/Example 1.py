import pandas as pd



course = ["DBMS", "DSA", "OOPS",
		"System Design", "CN", ]

# pass the period and staring index
webinar_date = pd.period_range('2020-08-15', periods=5)

# Determine Period Index and Column
# for DataFrame
df = pd.DataFrame(course, index=webinar_date, columns=['Course'])

df
