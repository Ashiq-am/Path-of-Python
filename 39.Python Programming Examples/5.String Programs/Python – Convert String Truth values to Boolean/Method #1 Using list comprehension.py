# Python3 code to demonstrate working of
# Convert String Truth values to Boolean
# Using list comprehension

# initializing lists
test_list = ["True", "False", "True", "True", "False"]

# printing string
print("The original list : " + str(test_list))

# using list comprehension to check "True" string
res = [ele == "True" for ele in test_list]

# printing results
print("The converted Boolean values : " + str(res))
