nums = [0, 1, 2, 3, 4, 5]
mapped = map(lambda x: x * x, nums)
filtered = filter(lambda x: x % 2, nums)
print(list(mapped))
print(list(filtered))
