''''''
'''In this example, a minimum length of string is set at 15 and ‘_’ are added to right side of string 
in Team column using the str.pad() method. ‘_’ is passed to fillchar parameters to add it instead 
of default whitespaces.'''


# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(how ='all', inplace = True)

# adding white spaces to left side
data["Team"]= data["Team"].str.pad(15, side ='right', fillchar ='_')

# output display
data
