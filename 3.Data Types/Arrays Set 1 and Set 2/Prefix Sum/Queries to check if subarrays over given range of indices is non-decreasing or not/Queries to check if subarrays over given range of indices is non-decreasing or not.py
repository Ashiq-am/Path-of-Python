# Python3 program for the above approach

# Function to perform queries to check if
# subarrays over a given range of indices
# is non-decreasing or not
def checkSorted(arr, N, Q):

	# Stores count of indices up to i
	# such that arr[i] > arr[i + 1]
	pre = [0]*(N)

	# Traverse the array
	for i in range(1, N):

		# Update pre[i]
		pre[i] = pre[i - 1] + (arr[i - 1] > arr[i])

	# Traverse the array Q[][]
	for i in range(len(Q)):
		l = Q[i][0]
		r = Q[i][1] - 1

		# If pre[r] - pre[l-1] exceeds 0
		if (pre[r] - pre[l - 1] == 0):
			print("Yes")
		else:
			print("No")

# Driver Code
if __name__ == '__main__':
	arr =[1, 7, 3, 4, 9]
	Q = [ [ 1, 2 ],[ 2, 4 ] ]
	N = len(arr)

	# Function Call
	checkSorted(arr, N, Q)
