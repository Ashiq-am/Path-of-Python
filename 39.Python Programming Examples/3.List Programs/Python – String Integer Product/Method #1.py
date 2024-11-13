# Python3 code to demonstrate working of
# String Integer Product
# using loop + int()

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= int(ele)
	return res

# initialize list
test_list = [['1', '4'], ['5', '6'], ['7', '10']]

# printing original list
print("The original list : " + str(test_list))

# String Integer Product
# using loop + int()
res = []
for sub in test_list:
	par_prod = prod(sub)
	res.append(par_prod)

# printing result
print("List after product of nested string lists : " + str(res))
