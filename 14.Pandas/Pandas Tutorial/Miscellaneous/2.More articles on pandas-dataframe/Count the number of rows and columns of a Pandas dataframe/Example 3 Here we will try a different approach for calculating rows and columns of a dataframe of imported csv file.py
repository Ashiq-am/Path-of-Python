# importing pandas
import pandas as pd

# importing csv file
df = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')

print(df.head())

# obtaining the shape
print("shape of dataframe", df.shape)

# obtaining the number of rows
print("number of rows : ", df.shape[0])

# obtaining the number of columns
print("number of columns : ", df.shape[1])
