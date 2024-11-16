# importing numpy lib
import numpy as np

# making a numpy array
arr = np.array([x for x in range(11, 20)])

print("Orignial array")
print(arr)

# making a blank list
new_arr = []

for x in arr:
# applying condition: appending even numbers
	if x % 2 == 0:
		new_arr.append(x)

# Converting new list into numpy array
new_arr = np.array(new_arr)
print("New array")
print(new_arr)
