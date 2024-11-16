# Create a numpy array from a list of
# numbers from 11 to 20
import numpy as np

a = np.array([11, 12, 13, 14, 15, 16, 17, 15,
			11, 12, 14, 15, 16, 17, 18, 19, 20])

# Get the index of elements with value less
# than 20 or greater than 12
print("The numbers index locations with the index of \
elements with value less than 20 or greater than 12 are ",
	np.where((a > 12) | (a < 20)))
