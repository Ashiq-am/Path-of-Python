# Python3 code to demonstrate
# Remove leading 0 from Strings List
# using startswith() + loop + list slicing

# Initializing list
test_list = ['012', '03', '044', '09']

# printing original list
print("The original list is : " + str(test_list))

# Remove leading 0 from Strings List
# using startswith() + loop + list slicing
for idx in range(len(test_list)):
	if test_list[idx].startswith('0'):
		test_list[idx] = test_list[idx][1:]

# printing result
print ("The string list after leading 0 removal : " + str(test_list))
