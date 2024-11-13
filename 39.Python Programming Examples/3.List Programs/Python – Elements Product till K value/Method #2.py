# Python 3 code to demonstrate
# Elements Product till K value
# using list comprehension

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing list
test_list = [1, 7, 5, 6, 3, 8]

# initializing k
k = 6

# printing list
print ("The list : " + str(test_list))

# using list comprehension
# Elements Product till K value
res = prod([i for i in test_list if i <= k])

# printing the intersection
print ("The product till K : " + str(res))
