nums = [0, 1, 2, 3, 4, 5]
mapped = (x * x for x in nums)
filtered = (x for x in nums if x % 2 == 1)
print(list(mapped))
print(list(filtered))
