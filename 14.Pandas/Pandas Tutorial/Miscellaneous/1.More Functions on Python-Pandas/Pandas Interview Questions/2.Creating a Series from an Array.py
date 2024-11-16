# import pandas and numpy
import pandas as pd
import numpy as np

# simple array
data = np.array(['g', 'e', 'e', 'k', 's'])

# convert array to Series
print(pd.Series(data))
