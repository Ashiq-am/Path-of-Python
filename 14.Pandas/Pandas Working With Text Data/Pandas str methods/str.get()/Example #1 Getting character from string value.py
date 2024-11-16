''''''
'''In this example, str.get() method is used to get a single character from the Name column. 
The null values have been removed using dropna() method and the series is converted to string type 
series using .astype() before applying this method. This method can be used to get one character 
instead of whole string. For example, getting M from Male and F from Female since there can be two 
inputs only, so doing this can save data.'''


# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# dropping null value columns to avoid errors
data.dropna(inplace = True)

# converting to string series
data["Name"]= data["Name"].astype(str)

# creating new column with element at 0th position in data["Team"]
data["New"]= data["Name"].str.get(0)

data
# display
