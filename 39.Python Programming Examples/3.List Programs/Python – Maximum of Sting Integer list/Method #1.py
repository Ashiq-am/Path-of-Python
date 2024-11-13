# Python3 code to demonstrate working of
# Maximum of Sting Integer
# using loop + int()

# initialize list
test_list = [['1', '4'], ['5', '6'], ['7', '10']]

# printing original list
print("The original list : " + str(test_list))

# Maximum of Sting Integer
# using loop + int()
res = []
for sub in test_list:
	par_max = 0
	for ele in sub:
		par_max = max(par_max, int(ele))
	res.append(par_max)

# printing result
print("List after maximization of nested string lists : " + str(res))
