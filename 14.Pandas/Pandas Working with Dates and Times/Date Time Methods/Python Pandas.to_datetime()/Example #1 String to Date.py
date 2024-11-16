''''''




"""In the following example, a csv file is read and the date column of Data frame is converted 
into Date Time object from a string object."""


# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("todatetime.csv")

# overwriting data after changing format
data["Date"]= pd.to_datetime(data["Date"])

# info of data
data.info()

# display
data
