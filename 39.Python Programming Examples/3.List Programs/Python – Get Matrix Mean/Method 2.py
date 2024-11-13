# Python3 code to demonstrate working of
# Matrix Mean
# Using mean() + zip() + list comprehension
from statistics import mean

# initializing lists
test_list = [[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]

# printing original list
print("The original list : " + str(test_list))

# zip() to get all elements
# mean() gives mean
# extracts column mean
res = [mean(idx) for idx in zip(*test_list)]

# extracts all elements mean
res = mean(res)

# printing result
print("Matrix Mean : " + str(res))
