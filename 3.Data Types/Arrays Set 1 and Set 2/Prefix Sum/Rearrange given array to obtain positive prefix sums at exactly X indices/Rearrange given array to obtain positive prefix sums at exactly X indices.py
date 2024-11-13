# Python3 program for the above approach

# Funtion to rearrange the array
# according to the given condition
def rearrange(a, n, x):

	# Using 2nd operation making
	# all values positive
	for i in range(n):
		a[i] = abs(a[i])

	# Sort the array
	a = sorted(a)

	# Assign K = N - K
	x = n - x;

	# Count number of zeros
	z = a.count(0)

	# If number of zeros if greater
	if (x > n - z):
		print("-1")
		return
	for i in range(0, n, 2):
		if x <= 0:
			break

		# Using 2nd operation convert
		# it into one negative
		a[i] = -a[i]
		x -= 1
	for i in range(n - 1, -1, -1):
		if x <= 0:
			break

		# Using 2nd operation convert
		# it into one negative
		if (a[i] > 0):
			a[i] = -a[i]
			x -= 1

	# Prthe array
	for i in range(n):
		print(a[i], end = " ")

# Driver Code
if __name__ == '__main__':
	arr = [0, -2, 4, 5, -3]
	K = 3
	N = len(arr)

	# Function Call
	rearrange(arr, N, K)
