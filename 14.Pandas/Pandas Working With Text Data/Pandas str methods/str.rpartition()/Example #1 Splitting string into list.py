''''''
'''In this example, the Team column is splitted into list on last occurrence of ‘o’. 
Before doing any operations, null rows are removed using .dropna() method to avoid errors.'''

# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(inplace=True)

# splitting and overwriting column
data["Team"] = data["Team"].str.rpartition("o", False)

# display
data
