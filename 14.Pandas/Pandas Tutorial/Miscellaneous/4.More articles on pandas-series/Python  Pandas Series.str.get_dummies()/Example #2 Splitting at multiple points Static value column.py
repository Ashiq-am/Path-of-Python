# importing pandas
import pandas as pd

# making data frame from csv at url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/employees.csv")

# string for new column
string ="Hello gfg family"

# creating new column
data["New_column"]= string

# creating dummies
df = data["New_column"].str.get_dummies("g")

# display
df.head(10)
