import pandas as pd

day = ["Sun", "Mon", "Tue",
	"Wed", "Thurs", "Fri", "Sat"]

# pass the period and staring index
daycode = pd.period_range('2020-08-15', periods=7)

# Determine Period Index and Column for DataFrame
df = pd.DataFrame(day, index=daycode, columns=['day'])

df
