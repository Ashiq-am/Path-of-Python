# Python code for the above approach

# Finds and prints the elements of
# the original array
def DecodeOriginalArray(presum, N):

	# Calculating elements of original array
	for i in range(N - 1, 0, -1):
		presum[i] = presum[i] - presum[i - 1];

	# Displaying elements of original array
	for i in range(N):
		print(presum[i], end= " ");

# Driver program to test above
presum = [45, 57, 63, 78, 89, 97];
N = len(presum)

# Function Call
DecodeOriginalArray(presum, N);

# This code is contributed by Saurabh Jaiswal
