# Trimmed Mean

from scipy import stats
import numpy as np

# array elements ranging from 0 to 19
x = np.arange(20)

print("Trimmed Mean :", stats.tmean(x))

print("\nTrimmed Mean by setting limit : ",
      stats.tmean(x, (2, 10)))
