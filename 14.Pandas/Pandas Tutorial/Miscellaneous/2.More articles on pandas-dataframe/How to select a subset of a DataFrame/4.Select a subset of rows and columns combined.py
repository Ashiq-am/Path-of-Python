# importing pandas library
import pandas as pd

# reading csv file
data = pd.read_csv("nba.csv")

# subset of dataframe
adults = data.loc[data["Age"] > 25, "Name"]

# display susbset
print(adults.head())
