# Function to check whether we can rearrange the array
def check(n, arr):
	odd = []
	even = []

	# Separate elements into odd and even lists
	for i in range(n):
		if arr[i] % 2 == 0:
			even.append(arr[i])
		else:
			odd.append(arr[i])

	# If the count of odd and even elements is not the same, it's not possible
	if len(odd) != len(even):
		return "NO"

	# Check if adjacent elements have an absolute difference of 1
	for i in range(len(odd)):
		if abs(odd[i] - even[i]) != 1:
			return "NO"

	return "YES"

# Driver code
if __name__ == "__main__":
	N = 6
	arr = [1, 1, 2, 2, 2, 3]

	# Function call
	print(check(N, arr))
