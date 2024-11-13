# PYthon program to read
# CSV file without csv module


import pandas as pd


#reading a csv file with pandas
data_frame = pd.read_csv("pokemon.csv")

#give the datatype of a pandas
# object
print(type(data_frame))

#this function gives us a
# brief view of the data.
print(data_frame.head)

#converting pandas dataframe
# to a numpy array.
arr = data_frame.to_numpy()
print(arr)
