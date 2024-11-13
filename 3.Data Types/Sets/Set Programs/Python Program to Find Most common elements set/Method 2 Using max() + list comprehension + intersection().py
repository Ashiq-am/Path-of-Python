# Python3 code to demonstrate working of
# Most common elements set
# Using loop + intersection()

# initializing list
test_list = [{4, 3, 5, 2}, {8, 4, 7, 2},
			{1, 2, 3, 4}, {9, 5, 3, 7}]

# printing original list
print("The original list is : " + str(test_list))

# initializing arg_set
arg_set = {9, 6, 5, 3}

# getting maximum length
max_len = max(len(sub.intersection(arg_set)) for sub in test_list)

# getting element matching length
res = [sub for sub in test_list if len(sub.intersection(arg_set)) == max_len][0]

# printing result
print("Set intersection : " + str(res))
