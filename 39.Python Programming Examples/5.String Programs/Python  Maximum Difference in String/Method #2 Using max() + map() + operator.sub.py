# Python3 code to demonstrate
# Maximum Difference in String
# using max() + map() + operator.sub
from operator import sub

# initializing string
test_string = '6543452345456987653234'

# printing original string
print("The original string : " + str(test_string))

# using max() + map() + operator.sub
# Maximum Difference in String
res = max(map(sub, map(int, test_string), map(int, test_string[1:])))

# print result
print("The maximum consecutive difference is : " + str(res))
