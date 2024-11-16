# importing pandas module
import pandas as pd

# importing csv from link
data = pd.read_csv("nba.csv")

# making copy of team column
new = data["Team"].copy()

# concatenating team with name column
# overwriting name column
data["Name"] = data["Name"].str.cat(new, sep=", ")

# display
data




"""

every string in the Address column having same index as string in Name 
column have been concatenated with separator “, “.

"""