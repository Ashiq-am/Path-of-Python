# importing pandas module
import pandas as pd

# making data frame csv at url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# sum of all salary
val = data['Salary'].sum()

val
