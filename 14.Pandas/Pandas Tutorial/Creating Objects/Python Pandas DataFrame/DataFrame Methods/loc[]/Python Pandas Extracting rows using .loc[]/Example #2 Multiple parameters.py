''''''
'''In this example, Name column is made as the index column and then two single rows are extracted at the 
same time by passing a list as parameter.'''



# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name")

# retrieving rows by loc method
rows = data.loc[["Avery Bradley", "R.J. Hunter"]]

# checking data type of rows
print(type(rows))

# display
rows
