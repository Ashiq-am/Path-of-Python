# Import library
import pandas as pd

# Reading csv file
df = pd.read_csv('StudentData.csv')

# using notnull() method ,it will return
# boolean values
mask = df.notnull()

# using dropna() method to drop NaN
# value rows
df = df.where(mask).dropna()

# Displaying result
print(df)
