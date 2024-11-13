# Python3 implementation of the approach

# Function to insert the character
def insert(arr: list, n: int, k: int) -> chr:

	# To store last position where
	# the insertion is done
	ind = 0

	# To store size of the string
	sz = 0

	# To store the modified string
	s = ""

	# To store characters
	ch = arr[0]

	# Add first character to the string
	s += ch

	# Update the size
	sz = 1

	# Update the index of last insertion
	ind = 0

	# Insert all other characters to the string
	for i in range(1, n):

		# Take the character
		ch = arr[i]

		# Take substring upto ind
		s1 = s[0:ind + 1]

		# Take modulo value of k with
		# the size of the string
		temp = k % sz

		# Check if we need to move to
		# the start of the string
		ro = temp - min(temp, sz - ind - 1)

		# If we don't need to move to start of the string
		if ro == 0:

			# Take substring from upto temp
			s2 = s[ind + 1:ind + 1 + temp]

			# Take substring which will be after
			# the inserted character
			s3 = s[ind + temp + 1:sz]

			# Insert into the string
			s = s1 + s2 + ch + s3

			# Store new inserted position
			ind = len(s1) + len(s2)

			# Store size of the new string
			# Technically sz + 1
			sz = len(s)

		# If we need to move to start of the string
		else:

			# Take substring which will before
			# the inserted character
			s2 = s[:ro]

			# Take substring which will be after
			# the inserted character
			s3 = s[ro:sz]

			# Insert into the string
			s = s2 + ch + s3

			# Store new inserted position
			ind = len(s2)

			# Store size of the new string
			# Technically sz + 1
			sz = len(s)

	# Return the required character
	if ind == 0:
		return s[sz - 1]
	else:
		return s[ind - 1]

# Driver Code
if __name__ == "__main__":
	arr = ['1', '2', '3', '4', '5']
	k = 2
	n = len(arr)

	# Function call
	print(insert(arr, n, k))
