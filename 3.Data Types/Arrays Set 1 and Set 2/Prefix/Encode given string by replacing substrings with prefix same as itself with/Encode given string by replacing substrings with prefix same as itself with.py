# Python code for the above approach

# Function to generate the encrypted string
def compress(str):

	# Stack to store encrypted string
	st = []

	# Variable to store length of string
	N = len(str)

	# Variable to point 1st and middle index
	i = 0
	j = (int)(N / 2)

	# Repeat the loop until
	# the entire string is checked
	while (j > 0):
		mid = j

		# Compare the substring
		# from index 0 to mid-1
		# with the rest of the substring
		# after mid.
		i=0
		while(str[i] == str[j] and i < mid):
			i += 1
			j += 1
		# If both substrings are equal
		# then repeat the same process
		# on this substring and store
		# the remaining string into stack
		if (i == mid):
			st.append(str[j:N])

			# Update the value of
			# string 'str' with the
			# longest repeating substring
			str = str[0:i]

			# Set the new string length to n
			N = mid

			# Initialize the 2nd pointer
			# from the mid of new string
			j = N // 2

		# If both substrings are not equal
		# then decrement the 2nd pointer by 1
		else:
			j = mid - 1

	# Pop all the elements from the stack
	# append a symbol '*' and store
	# in a output string
	while (len(st) != 0):
		str = str + '*' + st[len(st) - 1]
		st.pop()
	return str

# Driver code

# Declare and initialize the string
str = "zzzzzzz"
print(compress(str))

# This code is contributed by Saurabh jaiswal
