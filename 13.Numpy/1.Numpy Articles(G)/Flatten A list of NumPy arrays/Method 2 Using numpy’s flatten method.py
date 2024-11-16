# importing numpy as np
import numpy as np

# list of numpy array
list_array = [np.array([[1]]),
			np.array([[2]]),
			np.array([[3]]),
			np.array([[4]]),
			np.array([[5]]),
			np.array([[6]]),
			np.array([[7]]),
			np.array([[8]]),
			np.array([[9]]),
			np.array([[10]]),
			np.array([[11]]),
			np.array([[12]]),
			np.array([[13]]),
			np.array([[14]]),
			np.array([[15]]),
			np.array([[16]])]

# flatten the numpy array
flatten = np.array(list_array).flatten()

# printing the flatten array
print(flatten)
