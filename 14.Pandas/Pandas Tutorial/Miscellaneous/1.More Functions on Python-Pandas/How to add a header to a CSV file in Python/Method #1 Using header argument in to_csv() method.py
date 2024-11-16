# importing python package
import pandas as pd

# read contents of csv file
file = pd.read_csv("gfg.csv")
print("\nOriginal file:")
print(file)

# adding header
headerList = ['id', 'name', 'profession']

# converting data frame to csv
file.to_csv("gfg2.csv", header=headerList, index=False)

# display modified csv file
file2 = pd.read_csv("gfg2.csv")
print('\nModified file:')
print(file2)
