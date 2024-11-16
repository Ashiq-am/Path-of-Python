# importing pandas
import pandas as pd

# reading csv
df = pd.read_csv('data.csv')

# set the max columns to none
pd.set_option('display.max_columns', None)
