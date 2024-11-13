# Function to check if the given
# string is valid
def isValidString(s, k):

	# Getting size of the string
	n = len(s)

	# Initializing prefix arrays
	sum_arr = [0] * (n + 1)
	tot = [0] * (n + 1)

	# Precomputing prefix arrays
	for i in range(n):
		sum_arr[i + 1] += sum_arr[i]
		if s[i] == '0':
			sum_arr[i + 1] += 1
		if s[i] == '1':
			tot[i + 1] += 1
		tot[i + 1] += tot[i]

	# Initializing cnt to count total
	# number of valid substrings.
	cnt = 0
	for i in range(k, n + 1):

		# Condition for a valid substring
		if tot[i - k] == 0 and tot[n] - tot[i] == 0 and sum_arr[i] - sum_arr[i - k] == 0:

			# Incrementing cnt to keep
			# track of valid substrings.
			cnt += 1

	# Returning the answer
	if cnt == 1:
		return "Yes"
	return "No\n"

# Driver's code
if __name__ == '__main__':
	s = "00?1???10?"
	k = 5

	# Function Call
	print(isValidString(s, k))
# akashish__
