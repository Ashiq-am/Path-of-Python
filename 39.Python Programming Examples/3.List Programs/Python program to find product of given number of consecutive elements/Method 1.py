# getting product
def prod(sub):
	res = 1
	for ele in sub:
		res = ele * res
	return res


# initializing lists
test_list = [5, 6, 2, 1, 7, 5, 3]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

res = []
for idx in range(len(test_list) - K + 1):

	# getting product using external function
	res.append(prod(test_list[idx: idx + K]))

# printing result
print("Computed Products : " + str(res))
