# import numpy
import numpy as np

a = np.array([1.2, 2.4, 3.6, 4.8])
bins = np.array([1.0, 1.3, 2.5, 4.0, 10.0])

# using np.digitize() method
gfg = np.digitize(a, bins)

print(gfg)
