# Function to find absolute difference
# between left and right variable
def left_right_difference(arr):
	n = len(arr)
	res = []

	# Iterate in array arr[]
	for i in range(n):
		left_sum = 0
		right_sum = 0

		# calculate left sum
		for j in range(i):
			left_sum += arr[j]

		# calculate right sum
		for j in range(i + 1, n):
			right_sum += arr[j]

		# add absolute difference to result list
		res.append(abs(left_sum - right_sum))

	return res


# Driver code
if __name__ == "__main__":
	N = 4
	arr = [10, 4, 8, 3]

	# Function call
	ans = left_right_difference(arr)

	for i in range(N):
		print(ans[i], end=" ")
