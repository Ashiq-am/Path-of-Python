# Python3 code to demonstrate
# Lists Modulo
# using map()
from operator import mod

# initializing lists
test_list1 = [3, 5, 2, 6, 4]
test_list2 = [7, 3, 4, 1, 5]

# printing original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

# Lists Modulo
# using map()
res = list(map(mod, test_list1, test_list2))

# printing result
print ("The modulo list is : " + str(res))
