import numpy as np
import pandas as pd

# number of nan we want to add It will insert 3 nan vlaues to the data.....
n = 3

# creating dataset
data = np.random.randn(5, 5)

# choosing random indexes to put NaN
index_nan = np.random.choice(data.size, n, replace=False)

# adding nan to the data.
data.ravel()[index_nan] = np.nan
print(data)
