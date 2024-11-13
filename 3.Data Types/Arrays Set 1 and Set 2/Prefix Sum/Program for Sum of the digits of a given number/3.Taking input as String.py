# Python implementation of the above aprroach
def getSum(n):
	# Initializing sum to 0
	sum = 0
	# Traversing through string
	for i in n:
		# Converting char to int
		sum = sum + int(i)

	return sum


n = "123456789123456789123422"
print(getSum(n))
