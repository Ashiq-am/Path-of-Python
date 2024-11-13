# import pandas for reading csv file
import pandas as pd

#reading csv file
s = pd.read_csv("stock.csv", squeeze = True)

#using describe function
print(s.describe())

#using count function
print(s.idxmax())

#using idxmin function
print(s.idxmin())

#count of elements having value 3
print(s.value_counts().head(3))
