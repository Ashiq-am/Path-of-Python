''''''
'''In this example, a new series similar to Team column is created which has 2 spaces in both start 
and end of string. After that str.rstrip() method is applied and checked against a custom string with 
removed right side spaces.'''


# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# replacing team name and adding spaces in start and end
new = data["Team"].replace("Boston Celtics", " Boston Celtics ").copy()

# checking with custom removed space string
new.str.rstrip()==" Boston Celtics"
