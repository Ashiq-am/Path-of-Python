# Python code for the above approach:

# Function to calculate the possible
# number of ways to select 3 numbers
def numberOfWays(A, N):
	left_count_Zero,count1,left_count_One,count2 = 0,0,0,0
	ans = 0

	# Storing the right counts of
	# 1s and 2s in the array
	for i in range(N):
		if (A[i] == 1):
			count2 += 1
		else:
			count1 += 1

	# Traversing the array from left side
	for i in range(N):

		# If 1 is encountered,
		# looking for all combinations of
		# 0, 1, 0 possible
		if (A[i] == 1):

			# Number of ways to select one
			# 0 from left side * Number of
			# ways to select one 0 from right
			ans += (left_count_Zero * count1)

			# Decrement right_count of 1
			# and increment left_count of 1
			left_count_One += 1
			count2 -= 1

		# If 0 is encountered,
		# looking for all combinations
		# of 1, 0, 1 possible
		else:

			# Number of ways to select
			# one 1 from left side
			# * Number of ways to select a 1
			# from right
			ans += (left_count_One * count2)

			# Decrement right_count of 2
			# and increment left_count of 2
			left_count_Zero += 1
			count1 -= 1

	return ans

# Drivers code
arr = [0, 0, 1, 1, 0, 1]
N = 6

# Function call
print(numberOfWays(arr, N))

# This code is contributed by shinjanpatra
