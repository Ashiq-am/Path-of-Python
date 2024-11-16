import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name")


# retrieving two rows and two columns by iloc method
row2 = data.iloc [[3, 4], [1, 2]]



print(row2)
