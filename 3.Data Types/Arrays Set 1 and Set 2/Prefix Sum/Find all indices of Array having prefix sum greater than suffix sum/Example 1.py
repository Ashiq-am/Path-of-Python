# Python code to implement the above approach

class Solution:

	# Function to find the indices
	def solve(self, arr):
		ans = []

		# Total_size of the array
		size = len(arr)

		# Upto second last inddx
		for idx in range(size-1):
			left_sum = 0
			right_sum = 0

			# Calculate left sum
			for left_idx in range(idx + 1):
				left_sum += arr[left_idx]

			# Calculate right sum
			for right_idx in range(idx + 1,
								size, 1):
				right_sum += arr[right_idx]

			# check condition
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
