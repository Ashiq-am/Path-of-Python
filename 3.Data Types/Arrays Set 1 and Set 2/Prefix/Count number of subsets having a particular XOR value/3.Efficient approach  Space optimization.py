# Function to count the number of subsets with XOR equal to k
def subsetXOR(arr, k):
	n = len(arr)

	# Find the maximum element in the array
	max_ele = max(arr)

	# Calculate the maximum possible XOR value
	m = (1 << (int(max_ele).bit_length())) - 1

	# If k is greater than the maximum possible XOR value, return 0
	if k > m:
		return 0

	# Create a list to store the count of subsets with XOR equal to each possible value
	dp = [0] * (m + 1)
	dp[0] = 1 # There is one subset with XOR equal to 0 (empty subset)

	# Iterate over the array elements
	for i in range(1, n + 1):
		# Create a temporary list to store the previous row values
		temp = dp[:]

		# Update the dp list based on the previous row values
		for j in range(m + 1):
			# Calculate the count of subsets with XOR equal to j using the previous row values
			dp[j] = temp[j] + temp[j ^ arr[i - 1]]

	# Return the count of subsets with XOR equal to k
	return dp[k]

if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5]
	k = 4

	# Call the subsetXOR function and print the result
	print("Count of subsets is", subsetXOR(arr, k))
