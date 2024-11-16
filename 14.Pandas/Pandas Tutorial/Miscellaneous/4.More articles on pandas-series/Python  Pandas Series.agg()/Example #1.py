# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# creating random arr of 10 elements
arr=np.random.randn(10)

# creating series from array
series=pd.Series(arr)

# calling .agg() method
result=series.agg(lambda num : num + 2)

# display
print('Array before operation: \n', series,
	'\n\nArray after operation: \n',result)
