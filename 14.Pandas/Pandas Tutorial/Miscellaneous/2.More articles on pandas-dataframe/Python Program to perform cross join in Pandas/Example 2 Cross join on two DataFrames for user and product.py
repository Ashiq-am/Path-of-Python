# importing pandas module
import pandas as pd

# Define a dictionary containing user ID
data1 = {'Name': ["Rebecca", "Maryam", "Anita"],
         'UserID': [1, 2, 3]}

# Define a dictionary containing product ID
data2 = {'ProductID': ['P1', 'P2', 'P3', 'P4']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1, index=[0, 1, 2])

# Convert the dictionary into DataFrame
df1 = pd.DataFrame(data2, index=[2, 3, 6, 7])

# Now to perform cross join, we will create
# a key column in both the DataFrames to
# merge on that key.
df['key'] = 1
df1['key'] = 1

# to obtain the cross join we will merge on
# the key and drop it.
result = pd.merge(df, df1, on='key').drop("key", 1)

result
