# Python3 code to demonstrate working of
# Replace sublist with other in list
# Using list slicing ( When sublist index is given )

# initializing list
test_list = [4, 5, 6, 7, 10, 2]

# printing original list
print("The original list is : " + str(test_list))

# Replace list
repl_list_strt_idx = 1
repl_list_end_idx = 4
new_list = [11, 1]

# Replace sublist with other in list
# Using list slicing ( When sublist index is given )
test_list[repl_list_strt_idx : repl_list_end_idx] = new_list

# printing result
print("List after replacing sublist : " + str(test_list))
