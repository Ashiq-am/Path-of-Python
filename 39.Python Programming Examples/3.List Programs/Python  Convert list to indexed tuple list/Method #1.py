# Python3 code to demonstrate working of
# Convert list to indexed tuple
# Using list() + enumerate()

# initializing list
test_list = [4, 5, 8, 9, 10]

# printing list
print("The original list : " + str(test_list))

# Convert list to indexed tuple
# Using list() + enumerate()
res = list(enumerate(test_list))

# Printing result
print("List after conversion to tuple list : " + str(res))
