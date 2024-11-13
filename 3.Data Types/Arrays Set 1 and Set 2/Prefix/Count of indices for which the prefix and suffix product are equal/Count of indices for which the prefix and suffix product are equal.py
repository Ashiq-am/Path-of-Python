# Python Program to implement
# the above approach

# Function to calculate number of
# equal prefix and suffix product
# till the same indices
def equalProdPreSuf(arr):

	# Initialize a variable
	# to store the result
	res = 0

	# Initialize variables to
	# calculate prefix and suffix sums
	preProd = 1
	sufProd = 1

	# Length of array arr
	Len = len(arr)

	# Initialize an auxiliary array to
	# store suffix product at every index
	prod = [0] * Len

	# Traverse the array from right to left
	for i in range(Len-1, 0, -1):

		# Multiply the current
		# element to sufSum
		sufProd *= arr[i]

		# Store the value in prod
		prod[i] = sufProd

	# Iterate the array from left to right
	for i in range(Len):

		# Multiply the current
		# element to preProd
		preProd *= arr[i]

		# If prefix product is equal to
		# suffix product prod[i] then
		# increment res by 1
		if (preProd == prod[i]):

			# Increment the result
			res += 1

	# Return the answer
	return res


# Driver code

# Initialize the array
arr = [4, 5, 1, 1, -2, 5, -2]

# Call the function and
# print its result
print(equalProdPreSuf(arr))

# This code is contributed by gfgking.
