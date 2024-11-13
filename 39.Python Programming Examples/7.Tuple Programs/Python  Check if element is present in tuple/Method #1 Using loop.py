# Python3 code to demonstrate working of
# Check if element is present in tuple
# using loop

# initialize tuple
test_tup = (10, 4, 5, 6, 8)

# printing original tuple
print("The original tuple : " + str(test_tup))

# initialize N
N = 6

# Check if element is present in tuple
# using loop
res = False
for ele in test_tup :
	if N == ele :
		res = True
		break

# printing result
print("Does tuple contain required value ? : " + str(res))
