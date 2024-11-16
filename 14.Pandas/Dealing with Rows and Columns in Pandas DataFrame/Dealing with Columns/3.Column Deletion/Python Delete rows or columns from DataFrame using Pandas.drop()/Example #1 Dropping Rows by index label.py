''''''
'''In his code, A list of index labels is passed and the rows corresponding to those labels are 
dropped using .drop() method.'''



# importing pandas module
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name" )

# dropping passed values
data.drop(["Avery Bradley", "John Holland", "R.J. Hunter",
							"R.J. Hunter"], inplace = True)

# display
data
