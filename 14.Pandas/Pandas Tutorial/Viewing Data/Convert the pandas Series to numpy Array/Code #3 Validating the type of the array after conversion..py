# importing pandas
import pandas as pd

# reading csv
data = pd.read_csv("nba.csv")

data.dropna(inplace=True)

# creating series form weight column
gfg = pd.Series(data['Weight'].head())

# using to_numpy()
print(type(gfg.to_numpy()))
