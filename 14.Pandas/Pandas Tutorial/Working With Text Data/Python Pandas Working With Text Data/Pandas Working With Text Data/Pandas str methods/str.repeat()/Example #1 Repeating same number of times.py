''''''
'''In this example, a single integer is passed as repeats parameter and hence every string value in 
the series will be repeated same number of times. Before applying any operation, null values must be 
removed to avoid errors. Hence dropna() method is used to remove null values.'''


# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(how ='all', inplace = True)

# overwritting with repeated value
data["Team"]= data["Team"].str.repeat(2)

# display
data
