# declaring a string variable
str = "Geeksforgeeks is fun."

# index to remove character at
n = 4

# declaring an empty string variable for storing modified string
modified_str = ''

# iterating over the string
for char in range(0, len(str)):

	# checking if the char index is equivalent to n
	if(char != n):
		# append original string character
		modified_str += str[char]

print("Modified string after removing ", n, "th character ")
print(modified_str)
