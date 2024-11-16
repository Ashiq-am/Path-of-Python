''''''
'''In this example, the First Name and Last name is separated from the Name column and stored 
into separate columns in the data frame.'''

# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/chicago.csv")

# removing null values if any to avoid errors
data.dropna(how ='all', inplace = True)

# displaying top 5 rows of data
data.head()

# splitting at ', ' into Data frame
new = data["Name"].str.partition(", ", True)

# making seperate first name column from new data frame
data["First Name"]= new[2]

# making seperate last name column from new data frame
data["Last Name"]= new[0]

# Dropping old Name columns
data.drop(columns =["Name"], inplace = True)

# df display
data
