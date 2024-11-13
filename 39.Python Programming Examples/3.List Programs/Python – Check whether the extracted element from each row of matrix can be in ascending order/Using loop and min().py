# initializing list
test_list = [[3, 4, 6, 2], [3, 4, 9, 1], [8, 5, 4, 7], [9, 1, 2, 3]]

# printing original list
print("The original list is : " + str(test_list))

# initializing with min of 1st row
cur = min(test_list[0])

res = True
for sub in test_list[1:]:
	res = False

	# checking row for greater than previous minimum
	for idx in sub:
		if idx >= cur:
			res = True

			# storing new minimum
			cur = idx
			break

	if not res:
		break

# printing result
print("Is ascending list possible ? : " + str(res))
