import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name")


# retrieving multiple rows by iloc method
row2 = data.iloc [[3, 5, 7]]



row2
