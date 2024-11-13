# Python3 code to demonstrate working of
# Insert character after every K elements
# Using list comprehension + string slicing


# Function to Insert character
# in each duplicate string
# after every K elements
def insertCharacterAfterKelements(test_str, K, char):
	# list comprehension to bind logic in one.
	res = [test_str[:idx] + char + test_str[idx:]
		for idx in range(0, len(test_str), K)]

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
