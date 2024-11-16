# importing numpy lib
import numpy as np

# making a numpy array
arr = np.array([x for x in range(11, 40)])

print("Orignial array")
print(arr)

# using lambda to apply condition
new_arr = list(filter(lambda x: x > 15 and x % 2 == 0 and x % 10 != 0, arr))

# Converting new list into numpy array
new_arr = np.array(new_arr)
print("New array")
print(new_arr)
