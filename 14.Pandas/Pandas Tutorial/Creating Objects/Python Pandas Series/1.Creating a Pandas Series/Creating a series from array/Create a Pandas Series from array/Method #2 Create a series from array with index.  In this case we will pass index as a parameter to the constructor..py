# importing Pandas & numpy
import pandas as pd
import numpy as np

# numpy array
data = np.array(['a', 'b', 'c', 'd', 'e'])

# creating series
s = pd.Series(data, index =[1000, 1001, 1002, 1003, 1004])
print(s)
