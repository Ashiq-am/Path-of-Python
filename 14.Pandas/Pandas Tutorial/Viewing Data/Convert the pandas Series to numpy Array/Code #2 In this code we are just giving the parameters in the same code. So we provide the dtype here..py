# importing pandas
import pandas as pd

# read csv file
data = pd.read_csv("nba.csv")

data.dropna(inplace=True)

# creating series form weight column
gfg = pd.Series(data['Weight'].head())

# providing dtype
print(gfg.to_numpy(dtype='float32'))
