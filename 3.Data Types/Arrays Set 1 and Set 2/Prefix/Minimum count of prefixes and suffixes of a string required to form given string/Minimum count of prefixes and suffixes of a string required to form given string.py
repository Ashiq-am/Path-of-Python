# Python3 implementation for the above approach

# Function to find minimum number of
# concatenation of prefix and suffix
# of str2 to make str1
def partCount(str1, str2):

	# Initialize a set
	se = set()

	# Initialize a temporary string
	temp = ""

	l1 = len(str1)
	l2 = len(str2)

	# Iterate the string str2
	# from left to right
	for i in range(0, l2):

				# Add current character
				# to string temp
		temp += str2[i]

		# Insert the prefix into hashset
		se.add(temp)

		# Re-initialize temp string
		# to empty string
	temp = []

	# Iterate the string in reverse direction
	for i in range(l2 - 1, -1, -1):

				# Add current character to temp
		temp.append(str2[i])

		# Reverse the string temp
		temp.reverse()

		# Insert the suffix into the hashet
		se.add(''.join(temp))

		# Reverse the string temp again
		temp.reverse()

		# Initialize dp array to store the answer
	dp = [-1 for _ in range(len(str1) + 1)]
	dp[0] = 0

	# Check for all substrings starting
	# and ending at every indices
	for i in range(0, l1, 1):
		for j in range(1, l1 - i + 1):

						# HashSet contains the substring
			if (str1[i:i+j] in se):

				if (dp[i] == -1):
					continue

				if (dp[i + j] == -1):
					dp[i + j] = dp[i] + 1

				else:

					# Minimum of dp[i + j] and
					# dp[i] + 1 will be stored
					dp[i + j] = min(dp[i + j], dp[i] + 1)

		# Return the answer
	return dp[len(str1)]

# Driver Code
if __name__ == "__main__":

	str = "GEEKSFORGEEKS"
	wrd = "SFORGEEK"

	# Print the string
	print(partCount(str, wrd))

	# This code is contributed by rakeshsahni
