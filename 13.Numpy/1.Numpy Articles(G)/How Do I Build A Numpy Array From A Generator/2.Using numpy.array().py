# importing numpy library
import numpy as np

# generator function


def generator():
	n = 10
	for i in range(1, n+1):
		yield i


print(type(generator()))

if __name__ == "__main__":
	# calling the function and storing in our arrya
	arr = np.array(list(generator()), dtype=int)

	# Displaying the array
	print("Array : {}".format(arr))
	print(type(arr))
