# Python 3 Program to find an element
# such that sum of right side element
# is equal to sum of left side

# Function to Find an element in
# an array such that left and right
# side sums are equal


def findElement(arr, n):
	for i in range(1, n):
		leftSum = sum(arr[0:i])
		rightSum = sum(arr[i+1:])
		if(leftSum == rightSum):
			return arr[i]
	return -1


# Driver Code
if __name__ == "__main__":

	# Case 1
	arr = [1, 4, 2, 5]
	n = len(arr)
	print(findElement(arr, n))

	# Case 2
	arr = [2, 3, 4, 1, 4, 5]
	n = len(arr)
	print(findElement(arr, n))

	# Case 3
	arr = [1, 2, 3]
	print(findElement(arr, n))

# This code is contributed by Bhanu Teja Kodali
