# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# String to be searched in start of string
search ="G"

# boolean series returned with False at place of NaN
bool_series = data["College"].str.startswith(search, na = False)

# displaying filtered dataframe
data[bool_series]
