# importing pandas library
import pandas as pd

# reading csv file
data = pd.read_csv("nba.csv")

# subset of dataframe
above_25 = data[data["Age"] > 35]

# display subset
print(above_25.head())
