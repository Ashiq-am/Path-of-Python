# Python3 code to demonstrate
# to assign variables from list element
# using itertools.compress()
from itertools import compress

# initializing list
test_list = [1, 4, 5, 6, 7, 3]

# printing original list
print ("The original list is : " + str(test_list))

# using using itertools.compress()
# to assign variables from list element
var1, var2, var3 = compress(test_list, (0, 1, 0, 1, 0, 1, 0))

# printing result
print ("The variables are : " + str(var1) +
						" " + str(var2) +
							" " + str(var3))
