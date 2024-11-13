# Python3 code to demonstrate working of
# Standard deviation of list
# Using sum() + list comprehension

# initializing list
test_list = [4, 5, 8, 9, 10]

# printing list
print("The original list : " + str(test_list))

# Standard deviation of list
# Using sum() + list comprehension
mean = sum(test_list) / len(test_list)
variance = sum([((x - mean) ** 2) for x in test_list]) / len(test_list)
res = variance ** 0.5

# Printing result
print("Standard deviation of sample is : " + str(res))
