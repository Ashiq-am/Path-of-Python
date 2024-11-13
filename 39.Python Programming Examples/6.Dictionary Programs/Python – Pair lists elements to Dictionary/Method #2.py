# Python3 code to demonstrate working of
# Pair lists elements to Dictionary
# Using defaultdict() + zip()
from collections import defaultdict

# initializing lists
test_list1 = [1, 2, 3, 1, 1, 2, 3]
test_list2 = [[4, 5], [6, 7], [2, 3], [10, 12],
				[56, 43], [98, 100], [0, 13]]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Pair lists elements to Dictionary
# Using defaultdict() + zip()
res = defaultdict(list)
for ele1, ele2 in zip(test_list1, test_list2):
	res[ele1].extend(ele2)

# printing result
print("The Like elements compiled Dictionary is : " + str(dict(res)))
