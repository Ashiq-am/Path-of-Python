def digSum(n):

	if (n == 0):
		return 0
	if (n % 9 == 0):
		return 9
	else:
		(n % 9)

# Driver program to test the above function
n = 9999
print(digSum(n))