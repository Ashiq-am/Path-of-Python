''''''
'''In this example, the Team column is concatenated at the end of Name column with separator “, “. 
The Name column is overwritten with the new series and the data frame is then displayed.'''

# importing pandas module
import pandas as pd

# importing csv from link
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# making copy of team column
new = data["Team"].copy()

# concatenating team with name column
# overwriting name column
data["Name"]= data["Name"].str.cat(new, sep =", ")

# display
data
