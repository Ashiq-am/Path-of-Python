# importing pandas
import pandas as pd

# making data frame from csv at url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/employees.csv")

# making dataframe using get_dummies()
dummies = data["Team"].str.get_dummies(" ")

# display
dummies.head(10)
