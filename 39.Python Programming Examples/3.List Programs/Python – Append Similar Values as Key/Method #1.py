# Python3 code to demonstrate working of
# Append Similar Values as Key
# Using loop

# initializing list
test_list = ['Manjeet', 'Nikhil', 'Akshat', 'Akash',
			'Manjeet', 'Akash', 'Akshat', 'Manjeet']

# printing original list
print("The original list is : " + str(test_list))

# Append Similar Values as Key
# Using loop
res = dict()
for ele in test_list:
	try:
		res[ele].append(ele)
	except KeyError:
		res[ele] = [ele]

# printing result
print("The similar values dictionary is : " + str(res))
