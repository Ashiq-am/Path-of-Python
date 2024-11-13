# Python program to check encription validity
import math

# Function to calculate encryption validity
def encryption_validity(instruct_count, valid_period, keys):
	mp = {}
	maxi = 0

	# Count the frequency of each key
	for i in keys:
		mp[i] = mp.get(i, 0) + 1

	# Iterate through each key
	for i in range(len(keys)):
		num = keys[i]
		count = 0

		# Iterate through each possible divisor of num
		for j in range(1, int(math.sqrt(num)) + 1):
			# If j is a divisor of num and present in 'keys', count it
			if num % j == 0:
				if j in mp:
					count += mp[j]

				# If j is not equal to num/j and present in 'keys',
				# count num/j as well as divisors exist in pairs
				if j != num // j and num // j in mp:
					count += mp[num // j]

		maxi = max(count, maxi)

	var = instruct_count * valid_period

	if var >= maxi * 100000:
		return [1, maxi * 100000]

	return [0, maxi * 100000]

# Driver code
if __name__ == "__main__":
	instruct_count, valid_period, n = 1000, 10000, 4
	keys = [2, 4, 8, 2]
	res1 = encryption_validity(instruct_count, valid_period, keys)
	print(res1[0], res1[1])
	instruct_count, valid_period, n = 100, 1000, 2
	keys = [2, 4]
	res2 = encryption_validity(instruct_count, valid_period, keys)
	print(res2[0], res2[1])
# This code is contributed by
# Abhishek Kumar
