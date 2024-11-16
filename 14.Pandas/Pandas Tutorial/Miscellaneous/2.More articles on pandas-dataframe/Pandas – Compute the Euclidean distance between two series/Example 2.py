import pandas as pd
import numpy as np


x = pd.Series([1, 2, 3, 4, 5])
y = pd.Series([6, 7, 8, 9, 10])

# zip() function creates an iterator
# which aggregates elements from two
# or more iterables
dist = np.sqrt(np.sum([(a-b)*(a-b) for a, b in zip(x, y)]))

print("Series 1:")
print(x)

print("Series 2:")
print(y)

print("Euclidean distance between two series is:", dist)
