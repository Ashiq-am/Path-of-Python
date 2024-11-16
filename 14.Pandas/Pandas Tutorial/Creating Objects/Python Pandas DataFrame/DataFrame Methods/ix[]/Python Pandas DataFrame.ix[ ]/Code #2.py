# importing pandas package
import pandas as geek

# making data frame from csv file
data = geek.read_csv("nba.csv")

# Index slicing on Height column
print("After index slicing:")
x1 = data.ix[10:20, 'Height']
print(x1, "\n")

# Index slicing on Salary column
x2 = data.ix[10:20, 'Salary']
print(x2)
