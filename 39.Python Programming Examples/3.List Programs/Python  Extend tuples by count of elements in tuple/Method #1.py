# Python3 code to demonstrate working of
# Extend tuples by count in list
# using nested loop

# initialize list of tuple
test_list = [('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', )]

# printing original tuples list
print("The original list : " + str(test_list))

# Extend tuples by count in list
# using nested loop
res = []
for sub in range(len(test_list)):
	for ele in range(len(test_list[sub])):
		res.append(test_list[sub])

# printing result
print("The modified and extended list is : " + str(res))
