# Python3 code to demonstrate
# Maximum Pair Summation in String
# using max() + map() + operator.add
from operator import add

# initializing string
test_string = '6543452345456987653234'

# printing original string
print("The original string : " + str(test_string))

# using max() + map() + operator.add
# Maximum Pair Summation in String
res = max(map(add, map(int, test_string), map(int, test_string[1:])))

# print result
print("The maximum consecutive sum is : " + str(res))
