# Python3 code to demonstrate working of
# Remove square brackets from list
# using str() + list slicing

# initialize list
test_list = [5, 6, 8, 9, 10, 21]

# printing original list
print("The original list is : " + str(test_list))

# Remove square brackets from list
# using str() + list slicing
res = str(test_list)[1:-1]

# printing result
print("List after removing square brackets : " + res)
