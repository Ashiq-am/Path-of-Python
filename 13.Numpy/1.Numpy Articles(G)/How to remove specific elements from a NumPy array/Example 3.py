#import numpy as np
import numpy as np

# create an array with 10 elements
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# display a
print(a)

# delete 4 th element
print("remaining elements after deleting 4th element ",
	np.delete(a, 3))
