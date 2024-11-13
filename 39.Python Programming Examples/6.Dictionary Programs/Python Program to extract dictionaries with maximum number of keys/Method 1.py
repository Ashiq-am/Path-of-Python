# initializing list
test_list = [{'Gfg': 1}, {'Gfg': 1, 'is': 5, 'best': 4}, {'Gfg': 2, 'best': 9}]

# printing original list
print("The original list is : " + str(test_list))

res = dict()
max_len = 0
for sub in test_list:

	# comparing and updating maximum dictionary acc. to length
	if len(sub) > max_len:
		res = sub
		max_len = len(sub)

# printing result
print("Dictionary with maximum keys : " + str(res))
