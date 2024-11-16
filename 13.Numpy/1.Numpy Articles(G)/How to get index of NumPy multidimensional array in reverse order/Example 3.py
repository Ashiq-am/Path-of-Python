# import Modules
import numpy as np

# initialize parameters
a = np.array([[True, False, True, True],
			[False, False, True, False],
			[False, True, True, True],
			[True, False, False, True]])

reversed_array = a[:, ::-1]
max_val = np.argmax(reversed_array, axis=1)
num_rows = a.shape[1]
final_list = num_rows-1-max_val

print(final_list)
