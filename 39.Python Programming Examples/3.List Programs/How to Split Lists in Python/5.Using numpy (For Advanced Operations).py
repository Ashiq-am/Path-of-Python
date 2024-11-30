import numpy as np

# Splitting a list using numpy
li = [1, 2, 3, 4, 5, 6, 7]

# Number of Chunks
n = 3

# Keeping the chunks in list c after splitting
c = np.array_split(li, n)

print([list(c) for i in c])