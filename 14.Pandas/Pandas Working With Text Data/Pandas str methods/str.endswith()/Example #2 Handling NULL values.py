# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# String to be searched in end of string
search ="e"

# boolean series returned with False at place of NaN
bool_series = data["College"].str.lower().str.endswith(search, na = False)

# displaying filtered dataframe
data[bool_series]
