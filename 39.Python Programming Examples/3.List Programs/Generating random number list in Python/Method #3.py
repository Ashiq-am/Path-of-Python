# importing numpy module
import numpy as np

# print the list of 10 integers from 3 to 7
print(list(np.random.randint(low = 3,high=8,size=10)))

# print the list of 5 integers from 0 to 2
# if high parameter is not passed during
# function call then results are from [0, low)
print(list(np.random.randint(low = 3,size=5)))
