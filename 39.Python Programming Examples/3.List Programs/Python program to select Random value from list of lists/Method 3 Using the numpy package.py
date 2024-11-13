import numpy as np
import random

# initializing list
test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]

# printing original list
print("The original list is : " + str(test_list))

# initializing Row number
r_no = [0, 1, 2]

# Converting list to numpy array
arr = np.array(test_list)

# Generating random number from matrix
# using numpy random.choice() method
res = np.random.choice(arr[random.choice(r_no)])

# Printing result
print("Random number from Matrix Row : " + str(res))
