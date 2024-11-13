# Python3 code to demonstrate
# integrity sorting in two list
# using sorted() + zip() + lambda function
from operator import itemgetter

# initializing lists
test_list1 = [3, 4, 9, 1, 6]
test_list2 = [1, 5, 3, 6, 7]

# printing original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

# using sorted() + zip() + lambda function
# integrity sorting in two list
res = [list(i) for i in zip(*sorted(zip(test_list1, test_list2),
								key = lambda dual: dual[0]))]

# printing result
print ("The lists after integrity sort : " + str(res))
