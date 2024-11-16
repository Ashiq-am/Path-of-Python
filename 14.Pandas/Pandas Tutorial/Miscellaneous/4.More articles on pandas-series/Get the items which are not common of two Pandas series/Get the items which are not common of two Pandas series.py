# import the modules
import pandas as pd
import numpy as np

# create the series
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([3, 4, 5, 6, 7])

# union of the series
union = pd.Series(np.union1d(ser1, ser2))

# intersection of the series
intersect = pd.Series(np.intersect1d(ser1, ser2))

# uncommon elements in both the series
notcommonseries = union[~union.isin(intersect)]

# displaying the result
print(notcommonseries)
