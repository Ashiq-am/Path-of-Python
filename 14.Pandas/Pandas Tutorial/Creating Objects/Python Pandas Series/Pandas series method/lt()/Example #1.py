# importing pandas module
import pandas as pd

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# removing null values to avoid errors
data.dropna(inplace=True)

# other series
other = data["Weight"] / 10

# calling method and returning to new column
data["Age < Weight"] = data["Age"].lt(other)

# display
data
