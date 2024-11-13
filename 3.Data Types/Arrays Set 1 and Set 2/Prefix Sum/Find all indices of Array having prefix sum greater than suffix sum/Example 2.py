# Python code to implement the approach

class Solution:

	# Function to find the valid indices
	def solve(self, arr):
		ans = []

		# Total_size of the array
		size = len(arr)
		left_sum = 0
		total_sum = sum(arr)

		# Upto second last inddx
		for idx in range(size-1):

			# Add current element to
			# left_sum
			left_sum += arr[idx]

			# Calculate right_sum
			right_sum = total_sum - left_sum

			# Check condition
			if (left_sum > right_sum):
				ans.append(idx + 1)

		return(ans)

# Driver code
if __name__ == '__main__':
	obj = Solution()
	arr = [10, -3, 4, 6]
	ans = obj.solve(arr)
	for x in ans:
		print (x, end = " ")
