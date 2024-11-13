# Python3 code to demonstrate working of
# Convert String Truth values to Boolean
# Using map() + lambda

# initializing lists
test_list = ["True", "False", "True", "True", "False"]

# printing string
print("The original list : " + str(test_list))

# using map() to extend and lambda to check "True" string
res = list(map(lambda ele: ele == "True", test_list))

# printing results
print("The converted Boolean values : " + str(res))
