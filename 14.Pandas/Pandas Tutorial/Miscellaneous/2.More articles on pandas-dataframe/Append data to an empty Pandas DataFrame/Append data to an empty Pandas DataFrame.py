# importing the module
import pandas as pd

# creating the DataFrame of int and float
a = [[1, 1.2], [2, 1.4], [3, 1.5], [4, 1.8]]
t = pd.DataFrame(a, columns =["A", "B"])

# displaying the DataFrame
print(t)
print(t.dtypes)
