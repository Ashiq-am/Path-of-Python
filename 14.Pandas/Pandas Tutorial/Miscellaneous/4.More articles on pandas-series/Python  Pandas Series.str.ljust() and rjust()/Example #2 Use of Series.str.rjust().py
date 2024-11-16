# importing pandas module
import pandas as pd

# importing csv from link
# making data frame from csv
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/employees.csv")

# width of output string
width = 15

# character to put
char ="*"

# calling function and overwriting df
data["Team"]= data["Team"].str.rjust(width, char)

# display
data.head(10)
