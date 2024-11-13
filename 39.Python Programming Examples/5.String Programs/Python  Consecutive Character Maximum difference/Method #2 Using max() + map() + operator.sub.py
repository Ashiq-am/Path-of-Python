# Python3 code to demonstrate
# Consecutive Character Maximum difference
# using max() + map() + operator.sub
from operator import sub

# initializing string
test_string = '6543452345456987653234'

# printing original string
print("The original string : " + str(test_string))

# using max() + map() + operator.sub
# Consecutive Character Maximum difference
res = max(map(sub, map(int, test_string), map(int, test_string[1:])))

# print result
print("The maximum consecutive difference is : " + str(res))
