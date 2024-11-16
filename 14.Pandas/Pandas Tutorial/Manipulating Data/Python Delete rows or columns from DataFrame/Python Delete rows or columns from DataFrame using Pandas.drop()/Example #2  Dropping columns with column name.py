''''''
'''In his code, Passed columns are dropped using column names. axis parameter is kept 1 since 1 
refers to columns.'''


# importing pandas module
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name" )

# dropping passed columns
data.drop(["Team", "Weight"], axis = 1, inplace = True)

# display
data
