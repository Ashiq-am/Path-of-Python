# Python3 program to find minimum
# (or maximum) element in an array.
def getMin(arr, n):
	if(n==1):
		return arr[0]
	# If there is single element, return it.
	# Else return minimum of first element
	# and minimum of remaining array.
	else:
		return min(getMin(arr[1:], n-1), arr[0])
def getMax(arr, n):
	if(n==1):
		return arr[0]
	# If there is single element, return it.
	# Else return maximum of first element
	# and maximum of remaining array.
	else:
		return max(getMax(arr[1:], n-1), arr[0])

# Driver code
arr = [12, 1234, 45, 67, 1]
n = len(arr)
print("Minimum element of array: ",getMin(arr, n))
print("Maximum element of array: ",getMax(arr, n))


