# Python code to demonstrate working of
# Records list XOR
# Using reduce() + operator.ixor
from operator import ixor
from itertools import chain

# initializing list
test_list = [(4, 6), (2, ), (3, 8, 9)]

# printing original list
print("The original list is : " + str(test_list))

# Records list XOR
# Using reduce() + operator.ixor
temp = list(chain(*test_list))
res = reduce(ixor, temp)

# printing result
print("The Bitwise XOR of records list elements are : " + str(res))
