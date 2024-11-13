# Python3 code to demonstrate working of
# Sort while keeping Positive elements before negatives
# using sorted() + lambda

# initialize list
test_list = [4, -8, -6, 3, -5, 8, 10, 5, -19]

# printing original list
print("The original list is : " + str(test_list))

# Sort while keeping Positive elements before negatives
# using sorted() + lambda
res = sorted(test_list, key = lambda i: 0 if i == 0 else -1 / i)

# printing result
print("Result after performing sort operation : " + str(res))
