# Python3 code to demonstrate
# Remove empty List from List
# using filter()

# Initializing list
test_list = [5, 6, [], 3, [], [], 9]

# printing original list
print("The original list is : " + str(test_list))

# Remove empty List from List
# using filter
res = list(filter(None, test_list))

# printing result
print ("List after empty list removal : " + str(res))
