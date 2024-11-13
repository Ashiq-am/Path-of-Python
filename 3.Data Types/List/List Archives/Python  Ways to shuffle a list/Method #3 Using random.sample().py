# Python3 code to demonstrate
# shuffle a list
# using random.sample()

import random

# initializing list
test_list = [1, 4, 5, 6, 3]

# Printing original list
print ("The original list is : " + str(test_list))

# using random.sample()
# to shuffle a list
res = random.sample(test_list, len(test_list))

# Printing shuffled list
print ("The shuffled list is : " + str(res))
