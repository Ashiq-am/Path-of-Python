# importing pandas
import pandas as pd

# reading csv
data = pd.read_csv("nba.csv")

data.dropna(inplace=True)

# creating DataFrame form weight column
gfg = pd.DataFrame(data['Weight'].head())

# using to_numpy()
print(type(gfg.to_numpy()))
