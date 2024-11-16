''''''
'''In this example, ‘+’ has been added to both side of string using fillchar parameter in str.pad(). 
The width parameter is set to 20, so that the length of each string after padding becomes same.'''



# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(how ='all', inplace = True)

# adding white spaces to left side
data["Name"]= data["Name"].str.pad(20, side ='both', fillchar ='+')

# output
data
