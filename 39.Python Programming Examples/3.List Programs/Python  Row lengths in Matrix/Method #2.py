# Python3 code to demonstrate
# Row lengths in matrix
# using sum() + filter() + zip_longest()
from itertools import zip_longest

# initializing list
test_list = [[4, 5, 6], [7, 8], [2]]

# printing original list
print("The original list : " + str(test_list))

# using sum() + filter() + zip_longest()
# Row lengths in matrix
res = [sum(1 for idx in filter(None.__ne__, i))
			for i in zip_longest(*test_list)]

# print result
print("The row lengths in matrix : " + str(res))
