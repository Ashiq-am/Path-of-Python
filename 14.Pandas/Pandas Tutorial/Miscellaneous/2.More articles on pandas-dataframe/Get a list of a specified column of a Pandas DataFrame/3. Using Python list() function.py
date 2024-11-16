# importing pandas module
import pandas as pd

# making data frame from csv
data = pd.read_csv("nba.csv")
df = data.head(5)

# Converting a specific Dataframe
# column to list using list()
# function in Python
Name_List = list(df["Name"])

print("Converting name to list:")

# displaying list
Name_List
