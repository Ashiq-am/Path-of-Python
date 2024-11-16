# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# dropping null value columns to avoid errors
data.dropna(inplace = True)

# display
data["New Team"]= data["Team"].str.wrap(5)

# data frame display
data

# printing same index separately
print(data["Team"][120])
print("------------")
print(data["New Team"][120])
