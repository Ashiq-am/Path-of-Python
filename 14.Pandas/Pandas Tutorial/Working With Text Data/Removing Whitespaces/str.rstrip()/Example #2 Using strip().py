''''''
'''In this example, str.strip() method is used to remove spaces from both left and right side of the 
string. A new copy of Team column is created with 2 blank spaces in both start and the end. 
Then str.strip() method is called on that series. After that, it is compared with ” Boston Celtics “, 
” Boston Celtics” and “Boston Celtics ” to check if the spaces were removed from both sides or not.'''


# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# replacing team name and adding spaces in start and end
new = data["Team"].replace("Boston Celtics", " Boston Celtics ").copy()

# checking with custom string
new.str.strip()==" Boston Celtic"
new.str.strip()=="Boston Celtics"
new.str.strip()==" Boston Celtic"
