# importing pandas module
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name" )

# changing index cols with rename()
data.rename(index = {"Avery Bradley": "NEW NAME",
					"Jae Crowder":"NEW NAME 2"},
								inplace = True)
# display
data
