''''''
'''In this example, the name column is searched for ‘r’ using str.findall() method and output is stored 
in new column. Before doing any operations, null rows are dropped using .dropna() to avoid errors.'''

# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(inplace=True)

# string to be searched for
search = 'r'

# returning values and creating column
data["Findall(name)"] = data["Name"].str.findall(search)

# display
data.head(10)
