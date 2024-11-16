# Load library
import pandas as pd
df = pd.DataFrame()

# Create 6 dates
dates = pd.pd.Series(date_range('2/5/2019', periods = 6, freq ='M'))

print(dates)

# Extract days of week and then print
print(dates.dt.weekday_name)
