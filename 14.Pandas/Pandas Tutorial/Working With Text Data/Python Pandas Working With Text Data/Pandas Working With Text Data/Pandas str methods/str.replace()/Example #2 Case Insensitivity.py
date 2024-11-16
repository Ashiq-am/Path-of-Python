''''''
'''In this example, team name Boston Celtics is replaced by New Boston Celtics. In the parameters, 
instead of passing Boston, boston is passed (with ‘b’ in lower case) and the case is set to False, 
which means case insensitive. After that only teams having team name “New Boston Celtics” are displayed 
using .where() method.'''


# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# overwriting column with replaced value of age
data["Team"]= data["Team"].str.replace("boston", "New Boston", case = False)

# creating a filter for age column
# where age = "Twenty five"
filter = data["Team"]=="New Boston Celtics"

# printing only filtered columns
data.where(filter).dropna()
