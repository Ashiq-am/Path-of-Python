# Author: Amar Singh IIT BHU Varanasi

def generate(arr, curr, n, XOR, xorSubset):
	if curr == n:
		XOR[xorSubset] = XOR.get(xorSubset, 0) + 1 # Store XOR values in the map
		return
	generate(arr, curr + 1, n, XOR, xorSubset ^ arr[curr]) # Include current element in XOR
	generate(arr, curr + 1, n, XOR, xorSubset) # Exclude current element from XOR

def subsetXOR(arr, K):
	N = len(arr)
	P1, P2 = {}, {}

	generate(arr, 0, N // 2, P1, 0) # Generate XOR for the first half
	generate(arr, N // 2, N, P2, 0) # Generate XOR for the second half

	cnt = 0 # Counter for subsets with XOR equal to K

	for x in P1:
		find = K ^ x # Find corresponding value in the second half
		cnt += P2.get(find, 0) * P1[x] # Increment count with the product of occurrences

	return cnt # Return count of subsets with XOR equal to K

arr = [1, 2, 3, 4, 5] # Given array
k = 4 # XOR value to search for

print("Count of subsets is", subsetXOR(arr, k)) # Output the count of subsets

# Author: Amar Singh IIT BHU Varanasi
