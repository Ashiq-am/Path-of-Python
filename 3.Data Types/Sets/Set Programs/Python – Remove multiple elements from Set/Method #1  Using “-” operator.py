# Python3 code to demonstrate working of
# Remove multiple elements from Set
# Using "-" operator

# initializing set
test_set = {6, 4, 2, 7, 9}

# printing original set
print("The original set is : " + str(test_set))

# initializing remove elements
rem_ele = [2, 4, 8]

# using "-" operator to remove multiple elements
res = test_set - set(rem_ele)

# printing result
print("Set after removal : " + str(res))
