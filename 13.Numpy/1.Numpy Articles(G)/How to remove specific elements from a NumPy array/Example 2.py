# import numpy as np
import numpy as np

# create an array with 5
# elements
a = np.array([1, 2, 3, 4, 5])

# display a
print(a)

# delete 1 st element
print("remaining elements after deleting 1st and last element ",
	np.delete(a, [0, 4]))
