''''''
'''In this example, a single character ‘a’ is searched in each string of Name column using str.find() 
method. Start and end parameters are kept default. The returned series is stored in a new column so that 
the indexes can be compared by looking directly. Before applying this method, null rows are dropped 
using .dropna() to avoid errors.'''


# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# dropping null value columns to avoid errors
data.dropna(inplace = True)

# substring to be searched
sub ='a'

# creating and passsing series to new column
data["Indexes"]= data["Name"].str.find(sub)

# display
data
