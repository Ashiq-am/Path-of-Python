def solve(arr):
	# Initialize variables
	flag = False # Flag to check for the first occurrence of zero
	freq_map = {} # Frequency map to track prefix sum frequencies
	max_freq = 0 # Maximum frequency in any segment
	pref_sum = 0 # Prefix sum till any index
	ans = 0	 # Variable to store the answer

	# Loop through the array
	for num in arr:
		# Check if the current number is zero
		if num == 0:
			# If this is the first occurrence of zero
			if not flag:
				ans += freq_map.get(0, 0) # Add the frequency of prefix sum = 0
			else:
				ans += max_freq # Add the frequency of the most frequent element

			flag = True # Mark the occurrence of zero
			max_freq = 0 # Reset max_freq
			freq_map = {} # Clear the frequency map

		# Maintain the prefix sum
		pref_sum += num

		# Increase the frequency of the current prefix sum by 1
		freq_map[pref_sum] = freq_map.get(pref_sum, 0) + 1

		# Update max_freq with the frequency of the most frequent element
		max_freq = max(max_freq, freq_map[pref_sum])

	# If zero was not encountered in the array
	if not flag:
		ans += freq_map.get(0, 0) # Add the frequency of prefix sum = 0
	else:
		ans += max_freq # Add the frequency of the most frequent element

	return ans

def main():
	# Input array
	arr = [1, -1, 0, 2, 4, 2, 0, 1]

	# Call solve function and print the result
	print(solve(arr))

if __name__ == "__main__":
	main()
