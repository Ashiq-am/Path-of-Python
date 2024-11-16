''''''
'''In this example, two index label of rows are passed and all the rows that fall between those 
two index label have been returned (Both index labels Inclusive).'''


# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name")

# retrieving rows by loc method
rows = data.loc["Avery Bradley":"Isaiah Thomas"]

# checking data type of rows
print(type(rows))

# display
rows
