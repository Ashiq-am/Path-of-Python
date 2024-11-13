# Python3 code to demonstrate working of
# Index Directory of Elements
# Using dictionary comprehension + enumerate()

# initializing list
test_list = [7, 6, 3, 7, 8, 3, 6, 7, 8]

# printing original list
print("The original list is : " + str(test_list))

# getting each element index values
res = {key: [idx for idx, val in enumerate(test_list) if val == key]
	for key in set(test_list)}

# printing result
print("Index Directory : " + str(res))
