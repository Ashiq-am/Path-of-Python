# importing pandas module
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv")

for key, value in data.iteritems():
    print(key, value)
    print()
