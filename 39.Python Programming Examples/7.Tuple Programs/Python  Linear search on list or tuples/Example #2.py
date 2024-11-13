# Search function with parameter list name
# and the value to be searched
def search(Tuple, n):

	for i in range(len(Tuple)):
		if Tuple[i] == n:
			return True
	return False

# list which contains both string and numbers.
Tuple= (1, 2, 'sachin', 4, 'Geeks', 6)


# Driver Code
n = 'Geeks'

if search(Tuple, n):
	print("Found")
else:
	print("Not Found")
