# Python3 code to demonstrate
# clearing list as dict. value
# using loop + clear()

# initializing dict.
test_dict = {"Akash" : [1, 4, 3],
			"Nikhil" : [3, 4, 1],
			"Akshat" : [7, 8]}

# printing original dict
print("The original dict : " + str(test_dict))

# using loop + clear()
# clearing list as dict. value
for key in test_dict:
	test_dict[key].clear()

# print result
print("The dictionary after clearing value list : " + str(test_dict))
