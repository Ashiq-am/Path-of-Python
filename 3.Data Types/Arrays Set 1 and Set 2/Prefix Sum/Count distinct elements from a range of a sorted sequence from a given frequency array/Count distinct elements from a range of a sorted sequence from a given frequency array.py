# Python3 program for the above approach

# Function to find the first index
# with value is at least element
def binarysearch(array, right,
				element):

	# Update the value of left
	left = 1

	# Update the value of right

	# Binary search for the element
	while (left <= right):

		# Find the middle element
		mid = (left + right // 2)

		if (array[mid] == element):
			return mid

		# Check if the value lies
		# between the elements at
		# index mid - 1 and mid
		if (mid - 1 > 0 and array[mid] > element and
						array[mid - 1] < element):
			return mid

		# Check in the right subarray
		elif (array[mid] < element):

			# Update the value
			# of left
			left = mid + 1

		# Check in left subarray
		else:

			# Update the value of
			# right
			right = mid - 1

	return 1

# Function to count the number of
# distinct elements over the range
# [L, R] in the sorted sequence
def countDistinct(arr, L, R):

	# Stores the count of distinct
	# elements
	count = 0

	# Create the prefix sum array
	pref = [0] * (len(arr) + 1)

	for i in range(1, len(arr) + 1):

		# Update the value of count
		count += arr[i - 1]

		# Update the value of pref[i]
		pref[i] = count

	# Calculating the first index
	# of L and R using binary search
	left = binarysearch(pref, len(arr) + 1, L)
	right = binarysearch(pref, len(arr) + 1, R)

	# Print the resultant count
	print(right - left + 1)

# Driver Code
if __name__ == "__main__":

	arr = [ 3, 6, 7, 1, 8 ]
	L = 3
	R = 7

	countDistinct(arr, L, R)

# This code is contributed by ukasp
