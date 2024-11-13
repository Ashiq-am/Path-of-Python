# Python program for the above approach.

# Function to find the day
# with minimum stock price change
import sys

def find_the_day(arr, n):

	# Initialize and empty prefix_sum array
	prefix_sum = [0]*n
	prefix_sum[0] = arr[0]

	# Find the prefix sum of the array
	for i in range(1,n):
		prefix_sum[i] = arr[i] + prefix_sum[i - 1]

	# Initialize min_diff to store
	# the minimum diff of
	# left_avg and right_avg
	min_diff = sys.maxsize

	# Initializ the min_day to
	# store the day with min price change
	for i in range(n):

		# Calculate left avg till day i
		left_avg = prefix_sum[i] / (i + 1)

		# Calculate right avg after day i
		if (i == n - 1):
			right_avg = 0
		else:
			right_avg = (prefix_sum[n - 1]
						- prefix_sum[i])/ (n - i - 1)

		# Store the price change in the diff
		diff = left_avg - right_avg

		# Store the day with
		# minimum stock price change
		if (diff < min_diff):
			min_diff = diff
			min_day = i + 1

	# Print the day
	print(min_day)

# Driver code

arr = [ 15, 5, 10, 15, 5 ]
N = len(arr)

# Function call
find_the_day(arr, N)
