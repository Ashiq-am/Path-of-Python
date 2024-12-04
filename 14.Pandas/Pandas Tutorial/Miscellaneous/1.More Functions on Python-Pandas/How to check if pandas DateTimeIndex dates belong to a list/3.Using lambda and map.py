import pandas as pd

# Create a DataFrame with a DateTimeIndex
date_range = pd.date_range(start='2024-11-20', periods=7, freq='D')
df = pd.DataFrame({"temperature": [13, 24, 15, 13, 11, 10, 9]}, index=date_range)

# Define a list of holidays and convert to datetime
li = pd.to_datetime(['2024-11-22', '2024-11-25'])

# Use a lambda function to check if each date belongs to the list
df['is_in_list'] = df.index.map(lambda date: date in li)

print(df)