''''''
'''In this example, a sample data frame of 10 rows is created using .head() method. After that a 
list of 10 integers is created and passed to the repeat() function to repeat each string different 
number of times.'''

# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(how ='all', inplace = True)

# creating data of 10 rows
sample_data = data.head(10).copy()

# creating list of 10 int
repeat_list =[2, 1, 3, 4, 1, 5, 0, 6, 1, 2]

# calling repeat function
sample_data["Name"]= sample_data["Name"].str.repeat(repeat_list)

# displaying data
sample_data
