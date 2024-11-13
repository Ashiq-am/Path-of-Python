# Python3 code to demonstrate working of
# Maximum frequency in Tuple
# Using max() + Counter() + lambda
from collections import Counter

# initializing tuple
test_tuple = (6, 7, 8, 6, 7, 10)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Maximum frequency in Tuple
# Using max() + Counter() + lambda
res = max(Counter(test_tuple).items(), key=lambda ele: ele[1])

# printing result
print("Maximum element frequency tuple : " + str(res[0]))
