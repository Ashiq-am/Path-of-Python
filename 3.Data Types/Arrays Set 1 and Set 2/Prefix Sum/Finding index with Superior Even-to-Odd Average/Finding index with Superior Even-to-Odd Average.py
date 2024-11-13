def findValidIndex(arr):
	n = len(arr)

	# Initializing arrays for storing averages
	prefix_even_average = [0] * n
	suffix_odd_average = [0] * n

	# Initializing all required variables
	even_sum = 0
	even_average = 0
	even_length = 0
	odd_sum = 0
	odd_average = 0
	odd_length = 0
	answer = -1

	# Calculating prefix Even Averages for every index i in array arr
	for i in range(n):
		prefix_even_average[i] = even_average
		if arr[i] % 2 == 0:
			even_sum += arr[i]
			even_length += 1
			even_average = even_sum / even_length

	# Calculating suffix Odd Averages for every index i in array arr
	for i in range(n - 1, -1, -1):
		suffix_odd_average[i] = odd_average
		if arr[i] % 2 != 0:
			odd_sum += arr[i]
			odd_length += 1
			odd_average = odd_sum / odd_length

	# Finding whether there is a valid index or not
	for i in range(1, n - 1):
		if prefix_even_average[i] > suffix_odd_average[i]:
			# If we found a valid index then store it in the answer variable and break the loop
			answer = i
			break

	# Returning the final answer
	return answer

# Driver code
if __name__ == "__main__":
	arr = [4, 6, 1, 6, 5, 3]

	# Printing the answer
	print(findValidIndex(arr))
