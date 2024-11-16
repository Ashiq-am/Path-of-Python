# importing numpy lib
import numpy as np

# making a numpy array
arr = np.array([x for x in range(11, 40)])

print("Orignial array")
print(arr)

# making a blank list
new_arr = []

for x in arr:
	# applying two conditions: number is divisible by 2 and is greater than 15
	if x % 2 == 0 and x > 15:
		new_arr.append(x)

# Converting new list into numpy array
new_arr = np.array(new_arr)
print("New array")
print(new_arr)
