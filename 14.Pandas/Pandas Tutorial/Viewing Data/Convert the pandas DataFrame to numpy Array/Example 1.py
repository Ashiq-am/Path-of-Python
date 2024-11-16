# importing pandas
import pandas as pd

# reading the csv
data = pd.read_csv("nba.csv")

data.dropna(inplace=True)

# creating DataFrame form weight column
gfg = pd.DataFrame(data['Weight'].head())

# using to_numpy() function
print(gfg.to_numpy())
