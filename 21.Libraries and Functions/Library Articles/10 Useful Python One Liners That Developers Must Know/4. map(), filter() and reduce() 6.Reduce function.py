# max of all numbers in a list
from functools import reduce

nums = [2, 3, 5, 15]
max = reduce(lambda x, y: x if x >= y else y, nums)
print(max)

# Output 15
