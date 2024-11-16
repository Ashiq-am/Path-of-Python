# importing library
import numpy as np

# creating a numpy 2D array
x = np.array([[1, 2],
			[2, 3]])

print("Printing the Original array Content:\n",
	x)

# converting arrray elments to
# its corresponding negative value
r1 = np.negative(x)

print("Printing the negative value of the given array:\n",
	r1)
