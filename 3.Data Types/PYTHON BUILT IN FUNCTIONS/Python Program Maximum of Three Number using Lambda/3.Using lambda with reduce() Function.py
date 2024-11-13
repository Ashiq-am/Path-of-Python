from functools import reduce

num1 = 14
num2 = 18
num3 = 16

# reduce() with lambda to find maximum among three numbers
result = reduce(lambda x, y: x if x > y else y, [num1, num2, num3])

# print the result
print("Maximum number is:", result)
