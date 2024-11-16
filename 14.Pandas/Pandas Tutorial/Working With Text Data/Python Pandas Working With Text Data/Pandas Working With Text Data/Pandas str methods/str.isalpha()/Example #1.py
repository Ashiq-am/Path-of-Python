''''''
'''In this example, the isalpha() method is applied on the College column. Before that, the Null rows are 
removed using .dropna() method to avoid errors'''


# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(inplace = True)

# creating bool series
data["bool_series"]= data["College"].str.isalpha()

# display
data
