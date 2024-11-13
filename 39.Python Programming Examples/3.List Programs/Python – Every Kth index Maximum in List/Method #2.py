# Python3 code to demonstrate
# The max() helps to find max.
# using list comprehension + list slicing + max()

# initializing list
test_list = [1, 4, 5, 6, 7, 8, 9, 12]

# printing the original list
print ("The original list is : " + str(test_list))

# using list comprehension + list slicing + max()
# Edit every Kth element in list
# max of every 3rd element
res = max(test_list[0::3])

# printing result
print ("The max of every kth element : " + str(res))
