# Python3 code to demonstrate
# Sort alternate numeric and alphabet list
# using sorted() + key + lambda + isnumeric()
from itertools import zip_longest

# Initializing list
test_list = ['3', 'B', '2', 'A', 'C', '1']

# printing original list
print("The original list is : " + str(test_list))

# Sort alternate numeric and alphabet list
# using sorted() + key + lambda + isnumeric()
res = sorted(test_list, key = lambda ele : (int(ele), 0)
	if ele.isnumeric()
	else ((ord(ele) - 64) % 26, 1))

# printing result
print ("List after performing sorting : " + str(res))
