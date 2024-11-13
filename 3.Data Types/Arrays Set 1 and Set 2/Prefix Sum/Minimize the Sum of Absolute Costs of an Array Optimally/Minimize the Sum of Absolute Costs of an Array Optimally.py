import math


def minimize_absolute_differences(arr):
	# Create an array to store the absolute differences between consecutive costs.
	abs_arr = [0]

	# Initialize a variable to store the minimum sum of absolute differences.
	min_sum = float('inf')

	# Calculate the absolute differences between consecutive costs and store them in abs_arr.
	for i in range(1, len(arr)):
		abs_arr.append(abs(arr[i] - arr[i - 1]))

	# Set the last element of abs_arr to 0 because there's no next element to compare.
	abs_arr.append(0)

	# Calculate the sum of absolute differences.
	s = sum(abs_arr)

	# Iterate through each element in the input array.
	for i in range(len(arr)):
		if i - 1 < 0:
			# If there's no previous element, set left_sum to 0.
			left_sum = 0
			# Calculate the absolute difference between the cost halved and the next cost.
			right_sum = abs(math.floor(arr[i] / 2) - arr[i + 1])
		elif i + 1 > len(arr) - 1:
			# If there's no next element, set right_sum to 0.
			right_sum = 0
			# Calculate the absolute difference between the cost halved and the previous cost.
			left_sum = abs(math.floor(arr[i] / 2) - arr[i - 1])
		else:
			# Calculate the absolute difference between the cost halved and the previous cost.
			left_sum = abs(math.floor(arr[i] / 2) - arr[i - 1])
			# Calculate the absolute difference between the cost halved and the next cost.
			right_sum = abs(math.floor(arr[i] / 2) - arr[i + 1])

		# Calculate the total sum of left_sum and right_sum.
		total = left_sum + right_sum

		# Calculate the sum so far, including total, minus the absolute differences at the current and next elements.
		sum_sofar = s + total - (abs_arr[i] + abs_arr[i + 1])

		# Update the minimum sum with the minimum of the current sum_sofar and the previous minimum.
		min_sum = min(min_sum, sum_sofar)

	# Return the minimum sum of absolute differences.
	return min_sum


arr = [99, 102, 1, 45, 65]
result = minimize_absolute_differences(arr)
print(result)
