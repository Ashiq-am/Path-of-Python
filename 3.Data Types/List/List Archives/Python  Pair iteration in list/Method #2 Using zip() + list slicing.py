# Python3 code to demonstrate
# pair iteration in list
# using zip() + list slicing
from itertools import compress

# initializing list
test_list = [0, 1, 2, 3, 4, 5]

# printing original list
print ("The original list is : " + str(test_list))

# using zip() + list slicing
# to perform pair iteration in list
res = list(zip(test_list, test_list[1:] + test_list[:1]))

# printing result
print ("The pair list is : " + str(res))
