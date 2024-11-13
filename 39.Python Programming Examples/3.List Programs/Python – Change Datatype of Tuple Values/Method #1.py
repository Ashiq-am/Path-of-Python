# Python3 code to demonstrate working of
# Change Datatype of Tuple Values
# Using enumerate() + loop

# initializing list
test_list = [(4, 5), (6, 7), (1, 4), (8, 10)]

# printing original list
print("The original list is : " + str(test_list))

# Change Datatype of Tuple Values
# Using enumerate() + loop
# converting to string using str()
for idx, (x, y) in enumerate(test_list):
	test_list[idx] = (x, str(y))

# printing result
print("The converted records : " + str(test_list))
