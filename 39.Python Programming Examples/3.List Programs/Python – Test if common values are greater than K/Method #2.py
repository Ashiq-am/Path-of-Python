# Python3 code to demonstrate
# Test if common values are greater than K
# using sum()

# Initializing lists
test_list1 = ['Gfg', 'is', 'for', 'Geeks']
test_list2 = [1, 'Gfg', 2, 'Geeks']

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Initializing K
K = 2

# Test if common values are greater than K
# using sum()
res = sum(i in test_list1 for i in test_list2) >= 2

# printing result
print ("Are common elements greater than K ? : " + str(res))
