# importing pandas module
import pandas as pd

# importing csv from link
# making data frame from csv
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/employees.csv")

# width of output string
width = 12

# character to put
char ="_"

# calling function and overwriting df
data["Team"]= data["Team"].str.ljust(width, char)

# display
data.head(10)
