''''''
'''In this example, the college column is checked if elements have “G” in the start of string using 
the str.startswith() function. A Boolean series is returned which is true at the index position where 
string has “G” in the start.'''

# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# String to be searched in start of string
search ="G"

# boolean series returned
data["College"].str.startswith(search)
