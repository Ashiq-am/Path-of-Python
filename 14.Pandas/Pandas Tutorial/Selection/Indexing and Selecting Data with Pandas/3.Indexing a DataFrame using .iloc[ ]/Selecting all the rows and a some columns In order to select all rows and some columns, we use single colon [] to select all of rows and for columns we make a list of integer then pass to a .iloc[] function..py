import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name")


# retrieving all rows and some columns by iloc method
row2 = data.iloc [:, [1, 2]]



print(row2)
