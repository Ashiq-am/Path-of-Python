import numpy as np

# creating array
arr = np.array([2, 4, 6, 8, 10])

# creating copy of array
c = arr.copy()

# creating view of array
v = arr.view()

# printing base attribute of copy and view
print(c.base)
print(v.base)
