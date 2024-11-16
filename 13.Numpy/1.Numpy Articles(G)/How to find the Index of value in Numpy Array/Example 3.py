# create numpy array elements
import numpy as np

a = np.array([2, 3, 4, 5, 6, 45, 67, 34])

# display element index where values
# less than 20
print("element index where values less than 20 : ",
	np.where(a < 20))
