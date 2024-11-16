# importing numpy lib
import numpy as np

# making a numpy array
arr = np.array([x for x in range(11, 40)])

print("Orignial array")
print(arr)

# defining mask based on two conditions:
# array element must be greater than 15
# and must be a divisible by 2
mask = (arr > 15) & (arr % 2 == 0)

# making new array on conditons
new_arr = arr[mask]
print("New array")
print(new_arr)
