# Python3 code to demonstrate working of
# Convert List to Single valued Lists in Tuple
# Using map() + list() + zip() + tuple()

# initializing lists
test_list = [6, 8, 4, 9, 10, 2]

# printing original list
print("The original list is : " + str(test_list))

# Convert List to Single valued Lists in Tuple
# Using map() + list() + zip() + tuple()
res = tuple(map(list, zip(test_list)))

# printing result
print("Tuple after conversion : " + str(res))
