def pairings(test_list):
	if len(test_list) <= 1:
		return [test_list]

	# keeping 1st element and attaching every element with it
	parts = [[test_list[0]] + ele for ele in pairings(test_list[1:])]
	for idx in range(1, len(test_list)):

		# pairing all possible from second element
		parts.extend([[(test_list[0], test_list[idx])] +
					ele for ele in pairings(test_list[1: idx]
											+ test_list[idx + 1:])])

	return parts


# initializing list
test_list = [4, 7, 5, 1]

# printing original list
print("The original list is : " + str(test_list))

# calling util. fnction
res = pairings(test_list)

# printing result
print("Created partitions : " + str(res))
