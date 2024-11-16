# importing pandas module
import pandas as pd

# making data frame from csv
data = pd.read_csv("nba.csv")
df = data.head(5)

# Converting a specific Dataframe
# column to list using Series.tolist()
Name_list = df["Name"].tolist()

print("Converting name to list:")

# displaying list
Name_list
