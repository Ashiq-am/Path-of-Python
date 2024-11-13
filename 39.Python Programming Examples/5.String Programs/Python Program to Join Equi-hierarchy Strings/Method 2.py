from itertools import groupby


def hierjoin(test_list):

	# groups are formed for similar hierarchy using groupby
	return [idx for x, y in groupby(test_list, key=str.__instancecheck__)
			for idx in ([''.join(y)] if x else map(hierjoin, y))]


# initializing list
test_list = ["gfg ", " best ", [" for ", " all "],
			" all ", [" CS ", " geeks "]]

# printing original list
print("The original list is : " + str(test_list))

# calling recursion
res = hierjoin(test_list)

# printing result
print("The joined strings : " + str(res))
