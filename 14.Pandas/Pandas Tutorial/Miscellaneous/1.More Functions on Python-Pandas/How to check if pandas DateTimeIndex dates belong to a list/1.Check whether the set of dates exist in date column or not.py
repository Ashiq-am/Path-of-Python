import pandas as pd

# Create a DataFrame with a DateTimeIndex for one week
date_range = pd.date_range(start='2024-12-20', periods=7, freq='D')
df = pd.DataFrame({"temperature": [12, 14, 15, 13, 11, 10, 9]}, index=date_range)

# Define a list of holidays
holidays = ['2024-12-22', '2024-12-25']

# Convert holidays to datetime format
holidays = pd.to_datetime(holidays)

# Check if dates in the index belong to the list of holidays
df['is_holiday'] = df.index.isin(holidays)

print(df)