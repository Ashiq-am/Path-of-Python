''''''
"""In this data, the split function is used to split the Team column at every “t”. The parameter is 
set to 1 and hence, the maximum number of separations in a single string will be 1. The expand parameter
is False and that is why a series with List of strings is returned instead of a data frame."""

# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# dropping null value columns to avoid errors
data.dropna(inplace=True)

# new data frame with split value columns
data["Team"] = data["Team"].str.split("t", n=1, expand=True)

# df display
data
