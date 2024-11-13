# Python3 code to demonstrate
# Consecutive element maximum product
# using max() + map() + operator.mul
from operator import mul

# initializing string
test_string = '6543452345456987653234'

# printing original string
print("The original string : " + str(test_string))

# using max() + map() + operator.mul
# Consecutive element maximum product
res = max(map(mul, map(int, test_string), map(int, test_string[1:])))

# print result
print("The maximum consecutive product is : " + str(res))
