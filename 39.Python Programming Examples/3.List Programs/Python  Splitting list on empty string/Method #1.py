# Python3 code to demonstrate
# divide list to siblist on deliminator
# using index() + list slicing

# initializing list
test_list = ['Geeks', 'for', '', 'Geeks', 1, 2]

# printing original list
print("The original list : " + str(test_list))

# using index() + list slicing
# divide list to siblist on deliminator
temp_idx = test_list.index('')
res = [test_list[: temp_idx], test_list[temp_idx + 1: ]]

# print result
print("The list of sublist after separation : " + str(res))
