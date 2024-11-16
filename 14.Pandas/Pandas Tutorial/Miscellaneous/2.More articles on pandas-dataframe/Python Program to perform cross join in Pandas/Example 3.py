# importing pandas module
import pandas as pd

# Define a dictionary with two columns
data1 = {'col 1': [0, 1],
         'col 2': [2, 3]}

# Define another dictionary
data2 = {'col 3': [5, 6],
         'col 4': [7, 8]}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1, index=[0, 1])

# Convert the dictionary into DataFrame
df1 = pd.DataFrame(data2, index=[2, 3])

# Now to perform cross join, we will create
# a key column in both the DataFrames to
# merge on that key.
df['key'] = 1
df1['key'] = 1

# to obtain the cross join we will merge on
# the key and drop it.
result = pd.merge(df, df1, on='key').drop("key", 1)

result
