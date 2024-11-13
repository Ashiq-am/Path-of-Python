# Python 3 code to demonstrate
# check if list are identical
# using collections.Counter()
import collections

# initializing lists
test_list1 = [1, 2, 4, 3, 5]
test_list2 = [1, 2, 4, 3, 5]

# printing lists
print ("The first list is : " + str(test_list1))
print ("The second list is : " + str(test_list2))

# using collections.Counter() to check if
# lists are equal
if collections.Counter(test_list1) == collections.Counter(test_list2):
	print ("The lists are identical")
else :
	print ("The lists are not identical")
