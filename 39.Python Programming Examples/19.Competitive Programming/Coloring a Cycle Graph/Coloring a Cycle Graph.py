# Naive Python3 Program to
# find the number of colors
# required to color a cycle graph

# Function to find Color required.
def Color(vertices):

	result = 0

	# Check if number of vertices
	# is odd or even.
	# If number of vertices is even
	# then color require is 2 otherwise 3
	if (vertices % 2 == 0):
		result = 2
	else:
		result = 3

	return result

# Driver Code
if __name__=='__main__':
	vertices = 3
	print ("No. of colors require is:",Color(vertices))

# this code is contributed by Naman_Garg
