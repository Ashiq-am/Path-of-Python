''''''
'''Dataframe.loc[["row1", "row2"], ["column1", "column2", "column3"]]'''

import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name")

# retrieving two rows and three columns by loc method
first = data.loc[["Avery Bradley", "R.J. Hunter"],
				["Team", "Number", "Position"]]



print(first)
