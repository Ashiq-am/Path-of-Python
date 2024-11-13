# Python3 code to demonstrate working of
# Synchronized Split list with other
# Using map() + zip() + enumerate() + split()

# initializing list
test_list = [5, 6, 3, 7, 4]

# printing original list
print("The original list is : " + str(test_list))

# initializing String list
str_list = ['Gfg', 'is best', 'I love', 'Gfg', 'and CS']

# Synchronized Split list with other
# Using map() + zip() + enumerate() + split()
temp = list(map(list, zip(*[(idx, sub) for idx, val in
			enumerate(map(lambda x: x.split(), str_list), 1) for sub in val])))
res = []
for ele in temp[0]:
	res.append(test_list[ele - 1])

# printing result
print("Mapped list elements : " + str(res))
