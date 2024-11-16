import numpy as np

arr_m = np.arrange(12).reshape(2, 2, 3)

# Indexing
print(arr_m[0:3])
print()
print(arr_m[1:5:2,::3])
