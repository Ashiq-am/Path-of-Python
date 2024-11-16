# Load library
import pandas as pd

# Create data frame
df = pd.DataFrame()

# Create datetimes
df['date'] = pd.date_range('1/1/2012', periods = 1000, freq ='H')

# Set index
df = df.set_index(df['date'])

print(df.head(5))

# Select observations between two datetimes
x = df.loc['2012-1-1 04:00:00':'2012-1-1 12:00:00']

print(x)
