# importing pandas
import pandas as pd

# reading the csv
data = pd.read_csv("nba.csv")

data.dropna(inplace=True)

# creating series form weight column
gfg = pd.Series(data['Weight'].head())

# using to_numpy() function
print(type(gfg.to_numpy()))
