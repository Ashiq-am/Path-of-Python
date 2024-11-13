# Python program for the above approach
def rearrange_array(arr, N):
	# Initializing prefix sum
	prefix = 0

	ans = []
	checked = [True] * N

	# Sort the array
	arr.sort()
	ans.append(arr[0])
	prefix += arr[0]

	for i in range(1, N):
		if arr[i] > prefix:
			prefix += arr[i]
			ans.append(arr[i])
			checked[i] = False

	# The count of required numbers
	count = N - len(ans)

	for i in range(1, N):
		if checked[i]:
			ans.append(arr[i])

	print(count)

	for x in ans:
		print(x, end=" ")

	print()

# Main function
if __name__ == "__main__":
	arr = [4, 7, 5, 10]
	N = len(arr)
	rearrange_array(arr, N)
