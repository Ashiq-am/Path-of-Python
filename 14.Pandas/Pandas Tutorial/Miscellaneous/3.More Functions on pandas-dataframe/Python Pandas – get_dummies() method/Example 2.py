import pandas as pd
import numpy as np


# list
li = ['s', 'a', 't', np.nan]
print(pd.get_dummies(li))
