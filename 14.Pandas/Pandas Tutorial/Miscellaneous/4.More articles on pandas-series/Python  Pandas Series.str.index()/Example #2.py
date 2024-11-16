# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# dropping null value columns to avoid errors
data.dropna(inplace=True)

# extracting 5 rows
short_data = data.head().copy()

# calling str.index() method
try:
    short_data["Index Name"] = short_data["Name"].str.index("a")
except Exception as err:
    print(err)

# display
short_data
