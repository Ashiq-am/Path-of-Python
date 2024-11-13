# Python3 code to demonstrate working of
# Convert String to K characters row Matrix
# Using list comprehension + slicing


# Function to Convert String
# to K characters row Matrix
def convertToMatrix(test_str, K):
	# slicing strings
	temp = [test_str[idx: idx + K] for idx in range(0, len(test_str), K)]

	# conversion to list of characters
	res = [list(ele) for ele in temp]

	# printing result
	print("The converted Matrix : " + str(res))


# Driver Code
# initializing string
input_str = 'GeeksforGeeks is best'

# printing original string
print("The original string is : " + str(input_str))

# initializing K
K = 7

# calling the function
convertToMatrix(input_str, K)
