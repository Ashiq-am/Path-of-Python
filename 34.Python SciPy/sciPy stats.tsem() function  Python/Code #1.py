# Trimmed Standard error

from scipy import stats
import numpy as np

# array elements ranging from 0 to 19
x = np.arange(20)

print("Trimmed Standard error :", stats.tsem(x))

print("\nTrimmed Standard error by setting limit : ",
      stats.tsem(x, (2, 10)))
