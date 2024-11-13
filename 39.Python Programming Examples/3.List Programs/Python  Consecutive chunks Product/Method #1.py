# Python3 code to demonstrate
# Consecutive chunks Product
# using list comprehension + loop

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing list
test_list = [4, 7, 8, 10, 12, 15, 13, 17, 14]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + loop
# Consecutive chunks Product
res = [ prod(test_list[x : x + 3]) for x in range(0, len(test_list), 3)]

# printing result
print("The chunked product list is : " + str(res))
