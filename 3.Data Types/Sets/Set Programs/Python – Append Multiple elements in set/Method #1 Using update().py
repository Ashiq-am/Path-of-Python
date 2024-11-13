# Python3 code to demonstrate working of
# Append Multiple elements in set
# Using update()

# initializing set
test_set = {6, 4, 2, 7, 9}

# printing original set
print("The original set is : " + str(test_set))

# initializing adding elements
up_ele = [1, 5, 10]

# update() appends element in set
# internally reorders
test_set.update(up_ele)

# printing result
print("Set after adding elements : " + str(test_set))
