# importing numpy lib
import numpy as np

# making a numpy array
arr = np.array([x for x in range(11, 20)])

print("Orignial array")
print(arr)

# defining mask
mask = [True, False, True, False, True, True, False, False, False]

# making new array on conditons
new_arr = arr[mask]

print("New array")
print(new_arr)
