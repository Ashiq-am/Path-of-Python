''''''
'''The most important part in analyzing data is handling null values. str.cat() provides a way to handle 
null values through na_rep parameter. Whatever is passed to this parameter will be replaced at every
occurrence of null value.
In this example, college column is concatenated with team column. “No college” is passed to na_rep 
parameter to replace null with this string.

'''


# importing pandas module
import pandas as pd

# importing csv from link
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# making copy of team column
new = data["Team"].copy()

# string to replace null values with
na_string ="No College"

# concatenating team with name column
# overwriting name column
data["College"]= data["College"].str.cat(new, sep =", ", na_rep = na_string)

# display
data
