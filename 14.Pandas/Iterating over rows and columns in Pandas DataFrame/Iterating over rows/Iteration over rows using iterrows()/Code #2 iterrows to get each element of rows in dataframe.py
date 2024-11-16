# importing pandas module
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv")

for i, j in data.iterrows():
    print(i, j)
    print()
