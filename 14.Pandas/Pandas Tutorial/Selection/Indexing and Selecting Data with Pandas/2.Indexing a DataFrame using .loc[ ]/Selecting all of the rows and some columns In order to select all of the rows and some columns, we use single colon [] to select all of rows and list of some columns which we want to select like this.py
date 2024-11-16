''''''
'''Dataframe.loc[[:, ["column1", "column2", "column3"]]'''


import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name")

# retrieving all rows and some columns by loc method
first = data.loc[:, ["Team", "Number", "Position"]]



print(first)
