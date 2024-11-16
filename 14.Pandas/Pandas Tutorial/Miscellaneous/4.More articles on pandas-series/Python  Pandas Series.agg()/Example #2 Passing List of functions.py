# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating random arr of 10 elements
arr=np.random.randn(10)

# creating series from array
series=pd.Series(arr)

# creating list of function names
func_list=[min, max, sorted]

# calling .agg() method
# passing list of functions
result1, result2, result3= series.agg(func_list)

# display
print('Series before operation: \n', series)
print('\nMin = {}\n\nMax = {},\\n\nSorted Series:\n{}'.format(result1,result2,result3))
