''''''
'''In this example, the string length of Name column is calculated using str.len() method. 
The dtype of the Series is already string. So there is no need of data type conversion. 
Before doing any operations, null rows are removed to avoid errors.'''


# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# dropping null value columns to avoid errors
data.dropna(inplace = True)

# creating new column for len
# passing values through str.len()
data["Name Length"]= data["Name"].str.len()

# display
data
