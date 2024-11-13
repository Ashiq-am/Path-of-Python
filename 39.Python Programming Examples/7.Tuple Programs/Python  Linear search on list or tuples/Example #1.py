# Search function with parameter list name
# and the value to be searched
def search(list,n):

	for i in range(len(list)):
		if list[i] == n:
			return True
	return False

# list which contains both string and numbers.
list = [1, 2, 'sachin', 4,'Geeks', 6]

# Driver Code
n = 'Geeks'

if search(list, n):
	print("Found")
else:
	print("Not Found")
