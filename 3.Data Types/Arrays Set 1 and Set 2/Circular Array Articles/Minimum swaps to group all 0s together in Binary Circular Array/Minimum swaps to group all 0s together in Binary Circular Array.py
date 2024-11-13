# python3 program for the above approach

# Function to count min swap
# to get all zeros together
def minSwaps(nums, N):

	count_1 = 0

	if (N == 1):
		return 0

	for i in range(0, N):
		if (nums[i] == 0):
			count_1 += 1

	# Window size for counting
	# maximum no. of 1s
	windowsize = count_1
	count_1 = 0

	for i in range(0, windowsize):
		if (nums[i] == 0):
			count_1 += 1

	# For storing maximum count of 1s in
	# a window
	mx = count_1
	for i in range(windowsize, N + windowsize):
		if (nums[i % N] == 0):
			count_1 += 1
		if (nums[(i - windowsize) % N] == 0):
			count_1 -= 1
		mx = max(count_1, mx)

	return windowsize - mx

# Driver code
if __name__ == "__main__":

	nums = [1, 0, 1, 0, 0, 1, 1]
	N = len(nums)
	print(minSwaps(nums, N))
