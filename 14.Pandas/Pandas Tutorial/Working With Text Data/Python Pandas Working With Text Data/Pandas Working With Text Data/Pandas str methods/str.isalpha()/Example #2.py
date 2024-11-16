''''''
'''In this example, the isalpha() method is applied on Name column twice. First a bool series is 
created for the original name column, after that the white spaces are removed using str.replace() 
method and then a new bool_series is created again.'''

# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(inplace = True)

# creating bool series with original column
data["bool_series1"]= data["Name"].str.isalpha()

# removing white spaces
data["Name"]= data["Name"].str.replace(" ", "")

# creating bool series with new column
data["bool_series2"]= data["Name"].str.isalpha()

# display
data.head(10)
