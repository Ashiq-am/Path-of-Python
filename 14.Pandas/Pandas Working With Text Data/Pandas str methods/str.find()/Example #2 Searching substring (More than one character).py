''''''
'''In this example, ‘er’ substring will be searched in the Name column of data frame. The start parameter 
is kept 2 to start search from 3rd(index position 2) element.'''

# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# dropping null value columns to avoid errors
data.dropna(inplace = True)


# substring to be searched
sub ='er'

# start var
start = 2

# creating and passsing series to new column
data["Indexes"]= data["Name"].str.find(sub, start)

# display
data
