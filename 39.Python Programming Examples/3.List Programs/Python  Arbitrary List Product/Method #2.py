# Python3 code to demonstrate
# Arbitrary List Product
# using random.sample() + loop
import random

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# using random.sample() + loop
# Arbitrary List Product
res = prod(random.sample(range(1, 50), 7))

# printing result
print ("Arbitrary number product list is : " + str(res))
