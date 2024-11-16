#Import numpy module
import numpy as np

# iterable
iterable = (a*a for a in range(8))

arr = np.fromiter(iterable, float)

print("fromiter() array :",arr)
