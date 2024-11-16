''''''
'''In this example, all the values in age column having value 25.0 are replaced with “Twenty five” using 
str.replace()
After that, a filter is created and passed in .where() method to only display the rows which have 
Age = “Twenty five”.'''


# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# overwriting column with replaced value of age
data["Age"]= data["Age"].replace(25.0, "Twenty five")

# creating a filter for age column
# where age = "Twenty five"
filter = data["Age"]=="Twenty five"

# printing only filtered columns
data.where(filter).dropna()
