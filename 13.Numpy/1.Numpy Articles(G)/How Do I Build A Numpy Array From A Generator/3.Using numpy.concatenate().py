# importing numpy library
import numpy as np

# generator function
def generator():
	n = 10
	for i in range(1, n + 1):
		yield i

print(type(generator()))

if __name__ == "__main__":
	# calling the function and converting the
	#generator to a list
	gen_list = list(generator())
	arr = np.concatenate([gen_list], dtype=int)

	# Displaying the array
	print("Array: {}".format(arr))
	print("Type of Array:", type(arr))
