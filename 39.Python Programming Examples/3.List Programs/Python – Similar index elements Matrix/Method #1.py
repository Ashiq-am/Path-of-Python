# Python3 code to demonstrate
# Similar index elements Matrix
# using zip() + map()

# Initializing lists
test_list1 = [3, 4, 5]
test_list2 = [1, 2, 6]
test_list3 = [7, 9, 8]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))
print("The original list 3 is : " + str(test_list3))

# Similar index elements Matrix
# using zip() + map()
res = []
res += map(list, zip(test_list1, test_list2, test_list3))

# printing result
print("The matrix after cummulation is : " + str(res))
