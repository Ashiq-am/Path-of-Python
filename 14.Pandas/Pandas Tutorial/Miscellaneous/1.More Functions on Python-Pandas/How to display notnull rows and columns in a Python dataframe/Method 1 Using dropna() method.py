# Import library
import pandas as pd

# Reading csv file
df = pd.read_csv('StudentData.csv')

# using dropna() method
df = df.dropna()

# Printing result
print(df)
