# Python3 program for the above approach

# Function to count for each array
# element, the number of elements
# that are smaller than that element
def smallerNumbers(arr, N):

	# Stores the frequencies
	# of array elements
	hash = [0] * 100000

	# Traverse the array
	for i in range(N):

		# Update frequency of arr[i]
		hash[arr[i]] += 1

	# Initialize sum with 0
	sum = 0

	# Compute prefix sum of the array hash[]
	for i in range(1, 100000):
		hash[i] += hash[i - 1]

	# Traverse the array arr[]
	for i in range(N):

		# If current element is 0
		if (arr[i] == 0):
			print("0")
			continue

		# Print the resultant count
		print(hash[arr[i] - 1], end = " ")

# Driver Code
if __name__ == "__main__":

	arr = [ 3, 4, 1, 1, 2 ]
	N = len(arr)

	smallerNumbers(arr, N)

# This code is contributed by AnkThon
