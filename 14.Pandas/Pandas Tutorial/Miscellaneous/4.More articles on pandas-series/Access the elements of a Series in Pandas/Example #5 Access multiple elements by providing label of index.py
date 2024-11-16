# importing pandas module
import pandas as pd
import numpy as np

ser = pd.Series(np.arange(3, 15), index = list("abcdefghijkl"))

ser[['a', 'd', 'g', 'l']]
