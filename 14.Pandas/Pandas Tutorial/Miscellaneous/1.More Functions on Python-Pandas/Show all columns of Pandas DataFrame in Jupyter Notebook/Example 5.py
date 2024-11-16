# importing pandas
import pandas as pd

# reading the csv
df = pd.read_csv('data.csv')

# set max columns to none
pd.set_option("display.max_columns", None)

# set colwidth hidher
pd.set_option('display.max_colwidth', 100)
