# Python3 code to demonstrate
# Arbitrary List Product
# using list comprehension + randrange() + loop
import random

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# using list comprehension + randrange() + loop
# Arbitrary List Product
res = prod([random.randrange(1, 50, 1) for i in range(7)])

# printing result
print ("Arbitrary number product list is : " + str(res))
