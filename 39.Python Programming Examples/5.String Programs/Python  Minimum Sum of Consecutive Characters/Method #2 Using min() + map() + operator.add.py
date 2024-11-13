# Python3 code to demonstrate
# Minimum Sum of Consecutive Characters
# using min() + map() + operator.add
from operator import add

# initializing string
test_string = '6543452345456987653234'

# printing original string
print("The original string : " + str(test_string))

# using min() + map() + operator.add
# Minimum Sum of Consecutive Characters
res = min(map(add, map(int, test_string), map(int, test_string[1:])))

# print result
print("The minimum consecutive sum is : " + str(res))
