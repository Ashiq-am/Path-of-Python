# importing pandas and numpy
import pandas as pd
import numpy as np

ser = pd.Series(np.arange(3, 9), index=['a', 'b', 'c', 'd', 'e', 'f'])

print(ser[['a', 'd', 'g', 'l']])
