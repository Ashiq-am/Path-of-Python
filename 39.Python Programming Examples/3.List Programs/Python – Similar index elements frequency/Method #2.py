# Python3 code to demonstrate
# Similar index elements frequency
# using list comprehension + enumerate()

# Initializing lists
test_list1 = [1, 3, 5, 6, 8]
test_list2 = [4, 3, 6, 6, 10]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Similar index elements frequency
# using list comprehension + enumerate()
res = len([key for key, val in enumerate(zip(test_list1, test_list2)) if val[0] == val[1]])

# printing result
print ("Number of elements having similar index : " + str(res))
