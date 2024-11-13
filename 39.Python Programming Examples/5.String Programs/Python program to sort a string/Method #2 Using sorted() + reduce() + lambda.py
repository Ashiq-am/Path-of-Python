# Python code to demonstrate
# Sorting a string
# using sorted() + reduce() + lambda

# initializing string
test_string = "geekforgeeks"

# printing original string
print("The original string : " + str(test_string))

# using sorted() + reduce() + lambda
# Sorting a string
res = reduce(lambda x, y: x + y, sorted(test_string))

# print result
print("String after sorting : " + str(res))
