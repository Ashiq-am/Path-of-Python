from functools import reduce

nums = [1, 2, 3, 4]
ans = reduce(lambda x, y: x + y, nums)
print(ans)
