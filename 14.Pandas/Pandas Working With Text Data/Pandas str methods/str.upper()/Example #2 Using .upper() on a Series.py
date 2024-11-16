''''''
"""In this example, .upper() function is being called by the Team column and hence all the values in 
the Team column will be converted into upper case."""


# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees.csv")

# converting and overwriting values in column
data["Team"]= data["Team"].str.upper()

# display
data

