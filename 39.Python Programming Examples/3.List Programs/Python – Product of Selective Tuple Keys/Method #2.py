# Python3 code to demonstrate
# Product of Selective Tuple Keys
# using next() + list comprehension + loop

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing list of tuples
test_list = [('Nikhil', 1), ('Akash', 2), ('Akshat', 3), ('Manjeet', 4)]

# initializing selection list
select_list = ['Nikhil', 'Akshat']

# printing original list
print ("The original list is : " + str(test_list))

# printing selection list
print ("The selection list is : " + str(select_list))

# using next() + list comprehension + loop
# Product of Selective Tuple Keys
res = prod([next((sub[1] for sub in test_list if sub[0] == i), 0) for i in select_list])

# printing result
print ("The selective values product of keys : " + str(res))
