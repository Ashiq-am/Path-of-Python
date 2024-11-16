import pandas as pd
# importing pandas package

data = pd.read_csv("nba.csv")
# making data frame from csv file

new = data.copy()
# creating independent copy of data frame

popped_col = data.pop("Name")
# storing data in new var

new["New Col"]= popped_col
# creating new col and passing popped col

new
# display
