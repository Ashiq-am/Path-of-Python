# Python3 code to demonstrate
# integrity sorting in two list
# using sorted() + zip() + itemgetter()
from operator import itemgetter

# initializing lists
test_list1 = [3, 4, 9, 1, 6]
test_list2 = [1, 5, 3, 6, 7]

# printing original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

# using sorted() + zip() + itemgetter()
# integrity sorting in two list
res = [list(x) for x in zip(*sorted(zip(test_list1, test_list2),
										key = itemgetter(0)))]

# printing result
print ("The lists after integrity sort : " + str(res))
