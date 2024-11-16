''''''
'''In this example, the Name column is splitted into data frame on last occurrence 
(First from right side) of ‘a’ by keeping expand Parameter True. Before doing any operations, 
null rows are removed using .dropna() method to avoid errors.'''

# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(inplace=True)

# splitting and overwriting column
df = data["Name"].str.rpartition("a", True)

# display
df
