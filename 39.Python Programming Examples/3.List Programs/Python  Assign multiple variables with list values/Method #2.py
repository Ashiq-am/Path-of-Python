# Python3 code to demonstrate
# to assign variables from list element
# using itemgetter()
from operator import itemgetter

# initializing list
test_list = [1, 4, 5, 6, 7, 3]

# printing original list
print ("The original list is : " + str(test_list))

# using using itemgetter()
# to assign variables from list element
var1, var2, var3 = itemgetter(1, 3, 5)(test_list)

# printing result
print ("The variables are : " + str(var1) +
						" " + str(var2) +
							" " + str(var3))
