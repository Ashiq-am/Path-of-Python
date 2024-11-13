# Python3 code to demonstrate
# String Matrix Concatenation
# Using chain() + join()
from itertools import chain

# initializing list
test_list = [["geeksforgeeks", " is", " best"], [" I", " Love"], [" Gfg"]]

# printing original list
print("The original list : " + str(test_list))

# using chain() + join()
# String Matrix Concatenation
res = "".join(list(chain(*test_list)))

# print result
print("The Matrix Concatenation is : " + str(res))
