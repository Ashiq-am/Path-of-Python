# Python program to print all subsequence of a
# given string.

# set to store all the subsequences
st = set()

# Function computes all the subsequence of an string
def subsequence(str):

	# Iterate over the entire string
	for i in range(len(str)):

		# Iterate from the end of the string
		# to generate substrings
		for j in range(len(str),i,-1):
			sub_str = str[i: i+j]
			st.add(sub_str)

			# Drop kth character in the substring
			# and if its not in the set then recur
			for k in range(1,len(sub_str)):
				sb = sub_str

				# Drop character from the string
				sb = sb.replace(sb[k],"")
				subsequence(sb)

# Driver Code

s = "aabc"
subsequence(s)
for i in st:
	print(i,end = " ")
print()

# This code is contributed by shinjanpatra
