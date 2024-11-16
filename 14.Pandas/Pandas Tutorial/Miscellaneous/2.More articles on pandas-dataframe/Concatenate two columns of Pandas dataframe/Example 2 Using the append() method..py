# importing the module
import pandas as pd

# creating 2 DataFrames
first = pd.DataFrame([['one', 1], ['three', 3]], columns =['name', 'word'])
second = pd.DataFrame([['two', 2], ['four', 4]], columns =['name', 'word'])

# concatenating the DataFrames
dt = first.append(second, ignore_index = True)

# displaying the DataFrame
print(dt)
