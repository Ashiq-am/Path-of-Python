import pandas as pd

data = pd.read_csv("nba.csv")

g = pd.Series(data['Name'].head())
print(g.str.lower(), end ='\n\n')
print(g.str.capitalize())
