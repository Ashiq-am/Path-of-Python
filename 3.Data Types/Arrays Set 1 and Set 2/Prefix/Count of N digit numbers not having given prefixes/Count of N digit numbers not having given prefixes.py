# python Program to implement the above approach
import math

# Change int to long long in case of overflow!!
# Function to calculate total strings of length
# N without the given prefixes
def totalGoodStrings(N, prefixes):

		# Calculate total strings present
	total = int(math.pow(10, N) + 0.5)

	# Make a map and insert the prefixes with same
	# character in a vector
	mp = {}
	for i in range(0, len(prefixes)):
		if (ord(prefixes[i][0]) - ord('0')) in mp:
			mp[ord(prefixes[i][0]) - ord('0')].append(prefixes[i])

		else:
			mp[ord(prefixes[i][0]) - ord('0')] = [prefixes[i]]

		# Make a new vector of prefixes strings
	new_prefixes = []

	# Iterate for each starting character
	for x in mp:

		mn = N

		# Iterate through the vector to calculate
		# minimum size prefix
		for p in mp[x]:
			mn = min(mn, len(p))

		# Take all the minimum prefixes in the new
		# vector of prefixes
		for p in mp[x]:
			if (len(p) > mn):
				continue

			new_prefixes.append(p)

		# Iterate through the new prefixes
	for i in range(0, len(new_prefixes)):

				# Subtract bad strings
		total -= int(pow(10, N - len(new_prefixes[i])) + 0.5)

	return total

# Driver Code
if __name__ == "__main__":

	N = 5
	prefixes = ["1", "0", "911"]
	print(totalGoodStrings(N, prefixes))

	# This code is contributed by rakeshsahni
