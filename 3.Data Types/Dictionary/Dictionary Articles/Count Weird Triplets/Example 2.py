def count_triplets(arr):
	# Array to store distinct elements
	F = [0] * 1001

	# Getting the frequency of each distinct number
	for element in arr:
		F[element] += 1

	# Total possible triplets
	total_triplets = len(arr) * (len(arr) - 1) * (len(arr) - 2) // 6

	# Loop over the frequency array
	for freq in F:
		# Avoiding the case where all numbers in triplet are the same
		if freq < 2:
			continue

		# Handling the case where all 3 elements are the same (invalid triplets)
		all_same = freq * (freq - 1) * (freq - 2) // 6

		# Subtracting invalid triplets with respect to the current element
		total_triplets -= all_same

	# Returning the count of valid triplets
	return total_triplets

# Main Function
if __name__ == "__main__":
	# Input array A
	A = [5, 5, 2, 5]

	# Printing count of triplets by calling count_triplets() function
	print(count_triplets(A))
