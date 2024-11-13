# Python3 code to demonstrate
# List with most unique elements
# using key + max() + set()

# Initializing lists
test_list1 = [1, 3, 4, 4, 4, 3, 3, 2, 2, 1]
test_list2 = [1, 3, 4, 6, 7]
test_list3 = [4, 5, 4, 3, 6, 7, 8]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))
print("The original list 3 is : " + str(test_list3))

# List with most unique elements
# using key + max() + set()
temp = [set(test_list1), set(test_list2), set(test_list3)]
res = max(temp, key = len)

# printing result
print ("List with Most unique values : " + str(list(res)))
