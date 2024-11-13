# Python code to demonstrate working of
# Records list XOR
# Using reduce() + lambda + "^" operator + loops

# initializing list
from functools import reduce

test_list = [(4, 6), (2, ), (3, 8, 9)]

# printing original list
print("The original list is : " + str(test_list))

# Records list XOR
# Using reduce() + lambda + "^" operator + loops
temp = []
for sub in test_list:

    for ele in sub:
        temp.append(ele)
res = reduce(lambda x, y: x ^ y, temp)

# printing result
print("The Bitwise XOR of records list elements are : " + str(res))
