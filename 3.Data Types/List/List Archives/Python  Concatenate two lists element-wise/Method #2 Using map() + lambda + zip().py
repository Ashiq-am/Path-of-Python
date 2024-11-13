# Python code to demonstrate
# interlist element concatenation
# using map() + lambda + zip()

# initializing lists
test_list1 = ["Geeksfor", "i", "be"]
test_list2 = ['Geeks', 's', 'st']

# printing original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

# using map() + lambda + zip()
# interlist element concatenation
res = list(map(lambda i, j : i + j, zip(test_list1, test_list2)))

# printing result
print ("The list after element concatenation is : " + str(res))
