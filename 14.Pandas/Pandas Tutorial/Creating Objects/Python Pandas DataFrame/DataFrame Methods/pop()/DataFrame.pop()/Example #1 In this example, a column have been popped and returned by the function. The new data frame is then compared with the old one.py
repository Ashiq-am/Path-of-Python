import pandas as pd
# importing pandas package

data = pd.read_csv("nba.csv")
# making data frame from csv file

popped_col = data.pop("Team")
# storing data in new var

data
# display
