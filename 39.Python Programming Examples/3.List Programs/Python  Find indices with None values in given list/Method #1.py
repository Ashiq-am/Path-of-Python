# Python3 code to demonstrate
# finding None indices in list
# using list comprehension + enumerate

# initializing list
test_list = [1, None, 4, None, None, 5]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + enumerate
# finding None indices in list
res = [i for i in range(len(test_list)) if test_list[i] == None]

# print result
print("The None indices list is : " + str(res))
