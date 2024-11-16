# importing the pandas library
import pandas as pd

# Reading the csv file and storing it
# in a variable
df = pd.read_csv('Data.csv')

# Crosstab function is called
# 2 parameters are passed
# The table is stored in a variable
crosstb = pd.crosstab(df.Nationality, df.Handedness)
