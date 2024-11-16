# importing the pandas library
import pandas as pd

# Reading csv file
df = pd.read_csv('Data.csv')

# Creating crosstab
crosstb = pd.crosstab(df.Nationality, df.Handedness)

# Creating barplot
pl = crosstb.plot(kind="bar", stacked=True, rot=0)
