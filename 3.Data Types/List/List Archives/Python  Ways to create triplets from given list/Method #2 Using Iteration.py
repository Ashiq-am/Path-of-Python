# Python code to create triplets from list of words.

# List of word initialization
list_of_words = ['Geeks', 'for', 'Geeks', 'is',
				'best', 'resource', 'for', 'study']

# Output list initialization
out = []

# Finding length of list
length = len(list_of_words)

# Using iteration
for z in range(0, length-2):
	# Creating a temp list to add 3 words
	temp = []
	temp.append(list_of_words[z])
	temp.append(list_of_words[z + 1])
	temp.append(list_of_words[z + 2])
	out.append(temp)

# printing output
print(out)
