''''''
'''In this example, a copy of Name column is made. After that str.swapcase() is applied twice on
it and it is checked with original Series that whether it’s same or not.'''


# importing pandas module
import pandas as pd

# making data frame csv at url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(how ='all', inplace = True)

# making copy of series
new = data["Team"].copy()

# using swapcase() twice to interchange case
data["Team"] = data["Team"].str.swapcase().str.swapcase()

# creating a filter
filter = new == data["Team"]

# displaying values only where text at new == data["Team"]
data.where(filter)
