# cummulative frequency
from scipy import stats
import numpy as np

arr = [14, 31, 27, 27, 31, 13, 14, 13]

print ("Itemfrequency : \n", stats.itemfreq(arr))

print ("\n\nBincount : \n", np.bincount(arr))
