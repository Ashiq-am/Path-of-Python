# A mask example
import numpy as np
x = np.arange(5)
print(x)
mask = (x > 2)
print(mask)
x[mask] = -1
print(x)
