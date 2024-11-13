# Python3 code to demonstrate working of
# Remove Equilength and Equisum Tuple Duplicates
# Using nested loop

# initializing lists
test_list = [(4, 5, 6), (3, 0), (2, 1), (1, 2, 3), (5, 5, 5)]

# printing original list
print("The original list is : " + str(test_list))

# Remove Equilength and Equisum Tuple Duplicates
# Using nested loop
res = []
for sub in test_list:
	for sub1 in res:
		if len(sub) == len(sub1) and sum(sub) == sum(sub1):
			break
	else:
		res.append(sub)

# printing result
print("Tuples after filteration : " + str(res))
