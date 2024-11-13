# Python3 code to demonstrate working of
# Summation of String Integer lists
# using loop + int()

# initialize list
test_list = [['1', '4'], ['5', '6'], ['7', '10']]

# printing original list
print("The original list : " + str(test_list))

# Summation of String Integer lists
# using loop + int()
res = []
for sub in test_list:
	par_sum = 0
	for ele in sub:
		par_sum = par_sum + int(ele)
	res.append(par_sum)

# printing result
print("List after summation of nested string lists : " + str(res))
