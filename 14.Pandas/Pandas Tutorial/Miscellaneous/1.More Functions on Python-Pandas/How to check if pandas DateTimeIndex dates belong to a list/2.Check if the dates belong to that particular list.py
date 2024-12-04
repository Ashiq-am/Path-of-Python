import pandas as pd

# Create a DataFrame with a DateTimeIndex
date_range = pd.date_range(start='2024-12-01', periods=7, freq='D')
df = pd.DataFrame({"value": range(10, 80, 10)}, index=date_range)

# Define a list of dates to check
dates_to_check = pd.to_datetime(['2024-12-02', '2024-12-05', '2024-12-07'])

# Find the intersection of dates
common_dates = df.index.intersection(dates_to_check)

# Add a column to indicate whether each date is in the list
df['is_in_list'] = df.index.isin(common_dates)

print(df)