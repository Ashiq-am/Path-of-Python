# Python3 Program to find the size of
# largest subset of anagram

# Utility function to find size of
# largest subset of anagram
def largestAnagramSet(arr, n) :

	maxSize = 0
	count = {}

	for i in range(n) :

		# sort the string
		arr[i] = ''.join(sorted(arr[i]))

		# Increment the count of string
		if arr[i] in count :
			count[arr[i]] += 1
		else :
			count[arr[i]] = 1

		# Compute the maximum size of string
		maxSize = max(maxSize, count[arr[i]])

	return maxSize

# Driver code
arr = [ "ant", "magenta", "magnate", "tan", "gnamate" ]
n = len(arr)
print(largestAnagramSet(arr, n))

arr1 = [ "cars", "bikes", "arcs", "steer" ]
n = len(arr1)
print(largestAnagramSet(arr1, n))
