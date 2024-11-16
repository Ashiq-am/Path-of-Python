# import required modules
import pandas as pd
import numpy as np

# create dataset
s = pd.Series(list('abca'))

# display dataset
print(s)

# create dymmy variables
pd.get_dummies(s)
