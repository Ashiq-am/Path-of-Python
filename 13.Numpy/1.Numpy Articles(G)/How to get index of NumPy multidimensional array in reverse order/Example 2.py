#import Modules
import numpy as np

# initialize parameters
x = np.array([["Sam", "John", "Lilly"],
			["Sam", "Sam", "Kate"],
			["Jack", "John", "Sam"],
			["Sam", "Jack", "Rose"]])
num_cols = len(x[0])
result = []

# loop over each row
for row in x:
	row = np.flip(row)
	index = np.where(row == "Sam")
	result.append(index[0][0])

# get the final indexes
# Store the result as of the initial arrays
final_list = num_cols-np.array(result)-1

# print
print(final_list)
