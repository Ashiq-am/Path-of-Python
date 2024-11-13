# Python3 code to demonstrate
# converting binary list to integer
# using bit shift + | operator

# initializing list
test_list = [1, 0, 0, 1, 1, 0]

# printing original list
print ("The original list is : " + str(test_list))

# using bit shift + | operator
# converting binary list to integer
res = 0
for ele in test_list:
	res = (res << 1) | ele

# printing result
print ("The converted integer value is : " + str(res))
