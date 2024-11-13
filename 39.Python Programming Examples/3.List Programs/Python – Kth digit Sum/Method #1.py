# Python3 code to demonstrate working of
# Kth digit Sum
# Using loop + sum()

# initializing list
test_list = [5467, 34232, 45456, 22222, 3455]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

res = 0
for ele in test_list:

	# adding Kth digit
	res += int(str(ele)[K])

# printing result
print("Kth digit sum : " + str(res))
