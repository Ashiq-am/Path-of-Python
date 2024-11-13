def hierjoin(test_list):
	res = []
	temp = []
	val = None
	for sub in test_list:

		# if string then appended
		if type(sub) == str:
			temp.append(sub)

		# if list, the string is joined for hierarchy
		# recurred for inner list
		else:
			res.append(''.join(temp))
			temp = []
			val = hierjoin(sub)
			res.append(val)
	if temp != []:
		res.append(''.join(temp))
	return res


# initializing list
test_list = ["gfg ", " best ", [" for ", " all "],
			" all ", [" CS ", " geeks "]]

# printing original list
print("The original list is : " + str(test_list))

# calling recursion
res = hierjoin(test_list)

# printing result
print("The joined strings : " + str(res))
