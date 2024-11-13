# Python3 code to demonstrate
# Similar index elements frequency
# using sum() + zip()

# Initializing lists
test_list1 = [1, 3, 5, 6, 8]
test_list2 = [4, 3, 6, 6, 10]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Similar index elements frequency
# using sum() + zip()
res = sum(x == y for x, y in zip(test_list1, test_list2))

# printing result
print ("Number of elements having similar index : " + str(res))
