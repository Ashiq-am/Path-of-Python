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







"""In the following example, a new rank column is created which ranks 
the Name of every Player. All the values in Name column are unique and hence 
there is no need to describe a method"""
