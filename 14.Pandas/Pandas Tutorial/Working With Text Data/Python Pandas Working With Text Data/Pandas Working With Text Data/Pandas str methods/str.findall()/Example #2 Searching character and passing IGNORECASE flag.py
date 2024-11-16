''''''
'''In this example, the Name column is searched for ‘a’ and the IGNORECASE flag is passed. For that re 
module has to be imported too. The returned series from str.findall() method is stored in a New column.'''

# importing pandas module
import pandas as pd

# importing regex module
import re

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(inplace=True)

# string to be searched for
search = 'a'

# returning values and creating column
data["Findall(name)"] = data["Name"].str.findall(search, flags=re.I)

# display
data.head(10)
