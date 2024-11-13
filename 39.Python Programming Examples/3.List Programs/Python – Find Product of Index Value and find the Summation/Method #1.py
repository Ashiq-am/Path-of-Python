# Python3 code to demonstrate working of
# Index Value Product Sum
# Using loop + enumerate()

# initializing list
test_list = [5, 3, 4, 9, 1, 2]

# printing original list
print("The original list is : " + str(test_list))

res = 0
for idx, ele in enumerate(test_list):

	# updating summation of required product
	res += (idx + 1) * ele

# printing result
print("The computed sum : " + str(res))
