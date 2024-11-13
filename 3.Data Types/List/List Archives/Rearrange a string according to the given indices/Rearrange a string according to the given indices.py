# Python3 Program to implement
# the above approach

# Function to convert the strings
# to proper
def Convertstrings(s, index):
	a = []
	j = 0
	i = 0

	# Convert string to list
	for ii in str(s):
		a.append(ii)

	# Copy the list to another list
	b = a[:]

	# Move characters to specified indices
	while j < len(a) and i < len(index):
		k = index[i]
		temp = a[j]
		b[k] = temp
		j += 1
		i += 1
	s = ''

	# Convert the list to string
	for i in range(len(b)):
		s += b[i]

	# Print the answer
	print(s)


# Driver Code
s = "geeksforgeeks"
index = [5, 6, 7, 0, 1, 2, 8, 9, 10, 3, 4, 11, 12]
Convertstrings(s, index)
