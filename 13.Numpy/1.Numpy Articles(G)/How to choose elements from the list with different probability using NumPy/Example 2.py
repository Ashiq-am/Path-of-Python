# import numpy library
import numpy as np

# create a list
num_list = [10, 20, 30, 40, 50]

# choose index number-3rd element
# with 100% probability and other
# elements probability set to 0
# using p parameter of the
# choice() method so only
# 3rd index element selected
# every time in the list size of 3.
number_list = np.random.choice(num_list, 3,
						p = [0, 0, 0, 1, 0])

print(number_list)
