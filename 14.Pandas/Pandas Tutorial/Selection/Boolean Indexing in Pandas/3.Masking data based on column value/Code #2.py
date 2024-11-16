# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name")

# using greater than operator for filtering of data
print(data['Age'] > 25)
