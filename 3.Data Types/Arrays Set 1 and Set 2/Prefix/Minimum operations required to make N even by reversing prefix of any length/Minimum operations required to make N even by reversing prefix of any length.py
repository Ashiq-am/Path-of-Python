# python3 code for the above approach

# Function to find minimum number
# of steps required to make N an even number
def MinSteps(N):

	# Converting N into string
	s = str(N)
	ans = -1

	# Number of digits in N
	le = len(s)

	# If the number is even
	if ((ord(s[le - 1]) - ord('0')) % 2 == 0):
		ans = 0

	else:

		# If the first digit is even
		if ((ord(s[0]) - ord('0')) % 2 == 0):
			ans = 1

		else:

			# Checking if s contains
			# any even digits
			for i in range(0, le):
				if ((ord(s[i]) - ord('0')) % 2 == 0):
					ans = 2
					break

	# Printing the minimum number
	# of steps to make N an even number
	print(ans)

# Driver Code
if __name__ == "__main__":

	N = 36543

	MinSteps(N)

# This code is contributed by rakeshsahni
