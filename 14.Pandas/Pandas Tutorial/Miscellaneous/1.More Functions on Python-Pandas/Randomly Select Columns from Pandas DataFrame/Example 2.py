# import packages
import pandas as pd

# reading csv file
df =pd.read_csv('fossilfuels.csv')
pd.set_option('display.max_columns', None)
print(df.head())
print()

# randomly selecting columns
df = df.sample(n=5, axis='columns')
print(df.head())
