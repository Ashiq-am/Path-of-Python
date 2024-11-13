# Python3 code to demonstrate working of
# Remove multiple elements from Set
# Using difference_update()

# initializing set
test_set = {6, 4, 2, 7, 9}

# printing original set
print("The original set is : " + str(test_set))

# initializing remove elements
rem_ele = [2, 4, 8]

# using difference_update() to remove multiple elements
test_set.difference_update(set(rem_ele))

# printing result
print("Set after removal : " + str(test_set))
