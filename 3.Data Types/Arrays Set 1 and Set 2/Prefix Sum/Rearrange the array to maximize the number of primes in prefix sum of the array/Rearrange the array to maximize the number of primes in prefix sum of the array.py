# Python3 implementation of the approach

# Function to print the re-arranged array
def solve(a, n):

	ones, twos = 0, 0

	# Count the number of
	# ones and twos in a[]
	for i in range(n):

		# If the array element is 1
		if (a[i] == 1):
			ones+=1

		# Array element is 2
		else:
			twos+=1

	ind = 0

	# If it has at least one 2
	# Fill up first 2
	if (twos):
		a[ind] = 2
		ind+=1

	# Decrease the cnt of
	# ones if even
	if ones % 2 == 0:
		evenOnes = True
	else:
		evenOnes = False


	if (evenOnes):
		ones -= 1

	# Fill up with odd count of ones
	for i in range(ones):
		a[ind] = 1
		ind += 1


	# Fill up with remaining twos
	for i in range(twos-1):
		a[ind] = 2
		ind += 1

	# If even ones, then fill last position
	if (evenOnes):
		a[ind] = 1
		ind += 1

	# Print the rearranged array
	for i in range(n):
		print(a[i],end = " ")

# Driver code

a = [1, 2, 1, 2, 1]
n = len(a)
solve(a, n)
