# code to find union of more than two arrays
# import libraries
import numpy as np
from functools import reduce


array = reduce(np.union1d, ([1, 2, 3], [1, 3, 5],
							[2, 4, 6], [0, 0, 0]))
print("Union ", array)
