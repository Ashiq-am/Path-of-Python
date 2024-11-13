# initializing list
test_list = [(4, 5), (1, 3), (9, 4), (8, 2), (10, 1)]

# printing original list
print("The original list is : " + str(test_list))

# initializing start
start = 4

res = dict()
for sub in test_list:

	# assigning positional index
	res[start] = sub
	start += 1

# printing result
print("Constructed dictionary : " + str(res))
