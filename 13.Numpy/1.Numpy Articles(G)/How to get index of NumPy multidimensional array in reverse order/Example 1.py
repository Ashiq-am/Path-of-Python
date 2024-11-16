#import Modules
import numpy as np

# initialize parameters
x = np.array([[1, 2, 3, 4, 2],
			[2, 3, 4, 1, 5],
			[2, 2, 4, 3, 2],
			[1, 3, 4, 2, 4]])
num_cols = len(x[0])
result = []

# loop over each row
for row in x:
	row = np.flip(row)
	index = np.where(row == 2)
	result.append(index[0][0])

# get the final indexes
# Store the result as of the initial arrays
final_list = num_cols-np.array(result)-1

# print
print(final_list)
