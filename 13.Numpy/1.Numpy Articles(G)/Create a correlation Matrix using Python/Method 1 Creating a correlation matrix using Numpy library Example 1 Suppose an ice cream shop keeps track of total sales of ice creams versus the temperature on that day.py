import numpy as np


# x represents the total sale in
# dollers
x = [215, 325, 185, 332, 406, 522, 412,
	614, 544, 421, 445, 408],

# y represents the temperature on
# each day of sale
y = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1,
	19.4, 25.1, 23.4, 18.1, 22.6, 17.2]

# create correlation matrix
matrix = np.corrcoef(x, y)

# print matrix
print(matrix)
