import pandas as pd

# Create a DataFrame with a DateTimeIndex for a week
date_range = pd.date_range(start='2024-11-15', periods=7, freq='D')
df = pd.DataFrame({"sales": [100, 150, 200, 130, 170, 120, 180]}, index=date_range)

# Define a list of dates to check
dates_to_check = pd.to_datetime(['2024-11-16', '2024-11-19', '2024-11-20'])

# Use list comprehension to create a boolean array
df['is_in_list'] = [date in dates_to_check for date in df.index]

# Print the resulting DataFrame
print(df)