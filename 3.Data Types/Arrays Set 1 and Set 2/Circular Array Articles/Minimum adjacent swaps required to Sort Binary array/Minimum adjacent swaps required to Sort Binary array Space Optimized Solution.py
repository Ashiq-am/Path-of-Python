def minswaps(arr):
	count = 0
	num_unplaced_zeros = 0

	for index in range(len(arr)-1, -1, -1):
		if arr[index] == 0:
			num_unplaced_zeros += 1
		else:
			count += num_unplaced_zeros
	return count


arr = [0, 0, 1, 0, 1, 0, 1, 1]
print(minswaps(arr))
