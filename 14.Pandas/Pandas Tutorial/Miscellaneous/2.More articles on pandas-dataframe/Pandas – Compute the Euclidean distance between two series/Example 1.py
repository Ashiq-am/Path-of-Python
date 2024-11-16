import pandas as pd
import numpy as np


# create pandas series
x = pd.Series([1, 2, 3, 4, 5])
y = pd.Series([6, 7, 8, 9, 10])

# here we are computing every thing
# step by step
p1 = np.sum([(a * a) for a in x])
p2 = np.sum([(b * b) for b in y])

# using zip() function to create an
# iterator which aggregates elements
# from two or more iterables
p3 = -1 * np.sum([(2 * a*b) for (a, b) in zip(x, y)])
dist = np.sqrt(np.sum(p1 + p2 + p3))

print("Series 1:", x)
print("Series 2:", y)
print("Euclidean distance between two series is:", dist)
