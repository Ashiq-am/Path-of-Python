import functools

def findLen(string):
	return functools.reduce(lambda x, y: x+1, string, 0)

# Driver Code
string = 'geeksforgeeks'
print(findLen(string))
