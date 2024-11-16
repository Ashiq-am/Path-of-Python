# Python code demonstrate creating
# pandas DataFrame with indexed by

# DataFrame using arrays.
import pandas as pd

# initialise data of lists.
data = {'Name':['Tom', 'Jack', 'nick', 'juli'], 'marks':[99, 98, 95, 90]}

# Creates pandas DataFrame.
df = pd.DataFrame(data, index =['rank1', 'rank2', 'rank3', 'rank4'])

# print the data
df
