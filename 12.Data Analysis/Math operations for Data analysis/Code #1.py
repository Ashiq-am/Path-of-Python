# import pandas for reading csv file
import pandas as pd

#reading csv file
s = pd.read_csv("stock.csv", squeeze = True)

#using count function
print(s.count())

#using sum function
print(s.sum())

#using mean function
print(s.mean())

#calculatin average
print(s.sum()/s.count())

#using std function
print(s.std())

#using min function
print(s.min())

#using max function
print(s.max())

#using count function
print(s.median())

#using mode function
print(s.mode())
