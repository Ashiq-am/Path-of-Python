# Python program showing advanced
# and basic indexing
import numpy as np

a = np.array([[0, 1, 2], [3, 4, 5],
              [6, 7, 8], [9, 10, 11]])

print(a[1:2, 1:3])
print(a[1:2, [1, 2]])