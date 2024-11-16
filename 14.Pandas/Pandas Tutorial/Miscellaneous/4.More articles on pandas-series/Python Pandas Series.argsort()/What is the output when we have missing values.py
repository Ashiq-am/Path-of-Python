import pandas as pd

# importing pandas
import pandas as pd

# reading the csv
data = pd.read_csv("nba.csv")

# creating series form weight column
g = pd.Series(data['Weight'])
print(g)

gfg = g.argsort(axis=0, kind='mergesort', order=None)

print(gfg)
