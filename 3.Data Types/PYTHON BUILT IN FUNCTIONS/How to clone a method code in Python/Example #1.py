from statistics import median

# Using methodName.__code__.replace() method
median.__code__ = median.__code__.replace(co_posonlyargcount = 1)

print(median([1, 2, 3]))
