# sum of all numbers in a list
from functools import reduce

nums = [2, 3, 5, 15]
sum = reduce(lambda x, y: x+y, nums)
print(sum)

# Output 25
