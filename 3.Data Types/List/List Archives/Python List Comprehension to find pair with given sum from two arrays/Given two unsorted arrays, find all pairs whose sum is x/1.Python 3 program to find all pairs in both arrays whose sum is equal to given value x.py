# Python 3 program to find all
# pairs in both arrays whose
# sum is equal to given value x

# Function to print all pairs
# in both arrays whose sum is
# equal to given value x
def findPairs(arr1, arr2, n, m, x):

	for i in range(0, n):
		for j in range(0, m):
			if (arr1[i] + arr2[j] == x):
				print(arr1[i], arr2[j])

# Driver code
arr1 = [1, 2, 3, 7, 5, 4]
arr2 = [0, 7, 4, 3, 2, 1]
n = len(arr1)
m = len(arr2)
x = 8
findPairs(arr1, arr2, n, m, x)
