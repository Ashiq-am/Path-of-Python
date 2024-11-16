''''''
'''In this example, the Name column is splitted at the first occurrence of ‘, ‘. The expand parameter 
is kept False as to expand it into a list instead of Data Frame.'''

# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/chicago.csv")

# removing null values if any to avoid errors
data.dropna(how ='all', inplace = True)

# displaying top 5 rows of data
data.head()

# splitting at ', ' into list
data["Name"]= data["Name"].str.partition(", ", False)

# display
data
