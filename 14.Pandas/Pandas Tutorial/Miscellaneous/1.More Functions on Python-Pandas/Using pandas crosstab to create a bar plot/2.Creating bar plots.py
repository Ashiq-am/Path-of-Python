# importing the pandas library
import pandas as pd

# Reading the csv file and storing it in a variable
df = pd.read_csv('Data.csv')

# Creating crosstab
crosstb = pd.crosstab(df.Nationality, df.Handedness)

# Creating barplot
barplt = crosstb.plot.bar(rot=0)
