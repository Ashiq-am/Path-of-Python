def prefix_xor(arr, n, pre_xor):
	pre_xor[0] = arr[0]
	# Xoring present element with the previous element
	for i in range(1, n):
		pre_xor[i] = pre_xor[i - 1] ^ arr[i]

if __name__ == "__main__":
	arr = [10, 20, 10, 5, 15]
	n = len(arr)
	pre_xor = [0] * n

	# Function call
	prefix_xor(arr, n, pre_xor)

	print("Given Array:", end=" ")
	for i in range(n):
		print(arr[i], end=" ")
	print()

	print("Prefix XOR:", end=" ")
	for i in range(n):
		print(pre_xor[i], end=" ")
