# importing pandas
import pandas as pd

# reading the csv
data = pd.read_csv("nba.csv")

data.dropna(inplace=True)

# creating series form weight column
g = pd.Series(data['Weight'].head())
print(g)

gfg = g.argsort(axis=0, kind='mergesort', order=None)

print(gfg)
