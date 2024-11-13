# Python3 code to demonstrate
# Average of two lists
# using sum() + len() + "+" operator
from itertools import chain

# initializing lists
test_list1 = [1, 3, 4, 5, 2, 6]
test_list2 = [3, 4, 8, 3, 10, 1]

# printing the original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

# Average of two lists
# using sum() + len() + "+" operator
res = sum(chain(test_list1, test_list2)) / len(list(chain(test_list1, test_list2)))

# printing result
print ("The Average of both lists is : " + str(res))
