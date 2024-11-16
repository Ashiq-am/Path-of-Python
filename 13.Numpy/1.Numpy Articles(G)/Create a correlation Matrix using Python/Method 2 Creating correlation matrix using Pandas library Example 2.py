import pandas as pd


# create dataframe from file
dataframe = pd.read_csv("C:\\GFG\\sample.csv")

# show dataframe
print(dataframe)

# use corr() method on dataframe to
# make correlation matrix
matirx = dataframe.corr()

# print correlation matrix
print("Correlation Matrix is : ")
print(matrix)
