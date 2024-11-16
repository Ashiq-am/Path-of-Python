# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("nba.csv")

# overwriting column with replaced value of age
data["Age"] = data["Age"].replace(25.0, "Twenty five")

# creating a filter for age column
# where age = "Twenty five"
filter = data["Age"] == "Twenty five"

# printing only filtered columns
data.where(filter).dropna()
