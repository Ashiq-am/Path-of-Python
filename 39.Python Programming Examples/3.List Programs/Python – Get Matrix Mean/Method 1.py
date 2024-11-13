# Python3 code to demonstrate working of
# Matrix Mean
# Using list comprehension + sum() + len() + zip()

# initializing lists
test_list = [[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]

# printing original list
print("The original list : " + str(test_list))

# zip() to get all elements
# sum() / len() gives mean
# extracts column mean
res = [sum(idx) / len(idx) for idx in zip(*test_list)]

# extracts all elements mean
res = sum(res) / len(res)

# printing result
print("Matrix Mean : " + str(res))
