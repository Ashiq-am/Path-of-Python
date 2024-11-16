# importing pandas
import pandas as pd

# reading the csv
df = pd.read_csv('data.csv')

# get option to get maximum columns displayed
pd.get_option("display.max_columns")

# to get the number of columns
len(df.columns)
