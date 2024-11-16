# You may wish to select those elements whose
# sum of row is a multiple of 10.
import numpy as np

b = np.array([[5, 5], [4, 5], [16, 4]])
sumrow = b.sum(-1)
print(b[sumrow % 10 == 0])