# Python3 code to demonstrate
# to interleave lists
# using list slicing

# initializing lists
test_list1 = [1, 4, 5]
test_list2 = [3, 8, 9]

# printing original lists
print ("Original list 1 : " + str(test_list1))
print ("Original list 2 : " + str(test_list2))

# using list slicing
# to interleave lists
res = test_list1 + test_list2
res[::2] = test_list1
res[1::2] = test_list2

# printing result
print ("The interleaved list is : " + str(res))
