import pandas as pd

# Create DataFrames for Dataset 1 and Dataset 2
data1 = {'Name': ['John', 'Alice', 'Bob', 'Eve'],
         'Age': [25, 30, 22, 35],
         'Gender': ['Male', 'Female', 'Male', 'Female']}
df1 = pd.DataFrame(data1)

data2 = {'Name': ['John', 'Alice', 'Charlie', 'Eve'],
         'Age': [25, 32, 28, 35],
         'Gender': ['Male', 'Female', 'Male', 'Female']}
df2 = pd.DataFrame(data2)