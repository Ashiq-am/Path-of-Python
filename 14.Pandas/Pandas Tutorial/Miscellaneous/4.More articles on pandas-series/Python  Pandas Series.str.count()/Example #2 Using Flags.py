# importing pandas module
import pandas as pd

# importing module for regex
import re

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# String to be searched in start of string
search ="a"

# count of occurrence of a and creating new column
data["count"]= data["Name"].str.count(search, re.I)

# display
data
