# Python code to demonstrate
# largest possible number in list
# using sorted() + lambda
from functools import cmp_to_key

# initializing list
test_list = [23, 65, 98, 3, 4]

# printing original list
print ("The original list is : " + str(test_list))

# using sorted() + lambda
# largest possible number in list
res = sorted(test_list, key = cmp_to_key(lambda i, j: -1
				if str(j) + str(i) < str(i) + str(j) else 1))

# printing result
print ("The largest possible number : " + ''.join(map(str,res)))
