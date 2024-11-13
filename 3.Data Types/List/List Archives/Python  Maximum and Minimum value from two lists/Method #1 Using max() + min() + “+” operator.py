# Python3 code to demonstrate
# maximum and minimum values in two lists
# using max() + min() + "+" operator

# initializing lists
test_list1 = [1, 3, 4, 5, 2, 6]
test_list2 = [3, 4, 8, 3, 10, 1]

# printing the original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

# using max() + min() + "+" operator
# maximum and minimum values in two lists
max_all = max(test_list1 + test_list2)
min_all = min(test_list1 + test_list2)

# printing result
print ("The maximum of both lists is : " + str(max_all))
print ("The minimum of both lists is : " + str(min_all))
