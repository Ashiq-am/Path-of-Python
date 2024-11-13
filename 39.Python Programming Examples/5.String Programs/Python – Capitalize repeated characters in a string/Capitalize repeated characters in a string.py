# function for changing the
# repated characters to uppercase
def RepeatedUpper(s):

	# declaring dictionary
	dic = {}

	# Traversing the string
	for i in s:

		# If the character is already
		# present in dictionary then increment
		# the frequency of the character
		if i in dic:
			dic[i] = dic[i]+1

# If the character is not present in
# the dictionary then inserting
# the character in the dictionary
		else:
			dic[i] = 1
	ans = ''

	# traversing the string
	for i in s:

		# if the frequency of the character is
		# greater than one
		if dic[i] > 1:

			# change into uppercase
			i = i.upper()

		# appending each character to the ans
		ans = ans+i
	return ans


# Driver code
s = 'geeks for geeks'
# fuction call
print(RepeatedUpper(s))
