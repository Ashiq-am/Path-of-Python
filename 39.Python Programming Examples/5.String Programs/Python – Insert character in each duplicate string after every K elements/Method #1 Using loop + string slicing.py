# Python3 code to demonstrate working of
# Insert character after every K elements
# Using loop + string slicing


# Function to Insert character
# in each duplicate string
# after every K elements
def insertCharacterAfterKelements(test_str, K, char):
	res = []
	# using loop to iterate
	for idx in range(0, len(test_str), K):

		# appending all the results
		res.append(test_str[:idx] + char + test_str[idx:])

	return str(res)


# Driver Code
# initializing string
input_str = 'GeeksforGeeks'

# printing original string
print("The original string is : " + str(input_str))

# initializing K
K = 2

# initializing add char
add_chr = ";"

# printing result
print("The extracted strings : " +
	insertCharacterAfterKelements(input_str, K, add_chr))
