# Python program to Create a Dictionary with Key as First
# Character and Value as Words Starting with that Character

# Driver Code

# Declaring String Data
string_input = '''GeeksforGeeks is a Computer Science portal for geeks.
	It contains well written, well thought and well explained
	computer science and programming articles, quizzes etc.'''

# Storing words in the input as a list
words = string_input.split()

# Declaring empty dictionary
dictionary = {}

for word in words:

	# If key is not present in the dictionary then we
	# will add the key and word to the dictionary.
	if (word[0] not in dictionary.keys()):

		# Creating a sublist to store words with same
		# key value and adding it to the list.
		dictionary[word[0]] = []
		dictionary[word[0]].append(word)

	# If key is present then checking for the word
	else:

		# If word is not present in the sublist then
		# adding it to the sublist of the proper key
		# value
		if (word not in dictionary[word[0]]):
			dictionary[word[0]].append(word)

# Printing the dictionary
print(dictionary)
