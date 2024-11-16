# Load library
import pandas as pd

# Create data frame
df = pd.DataFrame()

# Create datetimes
df['date'] = pd.date_range('1/1/2012', periods = 1000, freq ='H')

print(df.head(5))

# Select observations between two datetimes
x = df[(df['date'] > '2012-1-1 01:00:00') &
	(df['date'] <= '2012-1-1 11:00:00')]

print(x)
