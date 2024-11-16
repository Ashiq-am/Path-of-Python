''''''
'''In this example, the Team column has been split at every occurrence of ” ” (Whitespace), into a 
list using str.split() method. Then the same column is overwritten with it. After that str.get() 
method is used to get elements in list at passed index.'''

# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# dropping null value columns to avoid errors
data.dropna(inplace = True)

# converting to string series
data["Team"]= data["Team"].astype(str)

# splitting at occurrence of whitespace
data["Team"]= data["Team"].str.split(" ", 1)

# displaying first element from list
data["Team"].str.get(0)

# displaying second element from list
data["Team"].str.get(1)
