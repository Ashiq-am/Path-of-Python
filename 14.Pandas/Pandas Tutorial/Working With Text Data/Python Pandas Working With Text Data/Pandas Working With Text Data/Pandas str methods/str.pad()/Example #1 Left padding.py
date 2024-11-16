''''''
'''In this example, a minimum length of string is set at 15 and whitespaces are added to left side 
of string in Team column using the str.pad() method. Since white spaces can’t be seen, they are 
compared with custom input string and the result is checked if it’s True or not for team name 
“Boston Celtics” only.'''


# importing pandas module
import pandas as pd

# making data frame from csv at url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/upload/nba.csv")

# removing null values to avoid errors
data.dropna(how ='all', inplace = True)

# adding white spaces to left side
data["Team"]= data["Team"].str.pad(15, side ='left')

# custom string
string =' Boston Celtics'

# checking if same or not
data["Team"]== string
