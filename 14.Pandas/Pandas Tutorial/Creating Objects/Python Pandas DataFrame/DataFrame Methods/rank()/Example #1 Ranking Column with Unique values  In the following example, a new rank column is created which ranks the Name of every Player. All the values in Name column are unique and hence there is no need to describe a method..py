# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv")

# creating a rank column and passing the returned rank series
data["Rank"] = data["Name"].rank()

# display
data

# sorting w.r.t name column
data.sort_values("Name", inplace = True)

# display after sorting w.r.t Name column
data
