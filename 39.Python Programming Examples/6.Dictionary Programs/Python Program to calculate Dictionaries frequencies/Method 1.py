# initializing list
test_list = [{'gfg': 1, 'is': 4, 'best': 9},
			{'gfg': 6, 'is': 3, 'best': 8},
			{'gfg': 1, 'is': 4, 'best': 9},
			{'gfg': 1, 'is': 1, 'best': 9},
			{'gfg': 6, 'is': 3, 'best': 8}]

# printing original list
print("The original list is : " + str(test_list))

res = []
for sub in test_list:

	flag = 0
	for ele in res:

		# checking for presence and incrementing frequency
		if sub == ele[0]:
			res[res.index(ele)] = (sub, ele[1] + 1)
			flag = 1

	if not flag:
		res.append((sub, 1))

# printing result
print("Dictionaries frequencies : " + str(res))
