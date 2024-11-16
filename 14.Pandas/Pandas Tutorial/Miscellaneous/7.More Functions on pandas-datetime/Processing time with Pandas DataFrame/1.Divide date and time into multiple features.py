# Load library
import pandas as pd

# calling DataFrame constructor
df = pd.DataFrame()

# Create 6 dates
df['time'] = pd.date_range('2/5/2019', periods = 6, freq ='2H')
print(df['time']) # print dataframe

# Extract features - year, month, day, hour, and minute
df['year'] = df['time'].dt.year
df['month'] = df['time'].dt.month
df['day'] = df['time'].dt.day
df['hour'] = df['time'].dt.hour
df['minute'] = df['time'].dt.minute

# Show six rows
df.head(6)
