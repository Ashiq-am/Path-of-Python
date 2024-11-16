# import packages
import pandas as pd

# reading csv file
df =pd.read_csv('fossilfuels.csv')
pd.set_option('display.max_columns', None)
print(df.head())

# randomly selecting columns
df = df.sample(axis='columns')
print(df)
