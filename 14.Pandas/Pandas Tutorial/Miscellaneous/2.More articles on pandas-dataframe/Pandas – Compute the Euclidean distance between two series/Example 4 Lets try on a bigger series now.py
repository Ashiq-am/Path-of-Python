import pandas as pd
import numpy as np


x = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = pd.Series([12, 8, 7, 5, 6, 5, 3, 9, 7, 1])
dist = np.sqrt(np.sum([(a-b)*(a-b) for a, b in zip(x, y)]))

print("Series 1:")
print(x)

print("Series 2:")
print(y)

print("Euclidean distance between two series is:", dist)
