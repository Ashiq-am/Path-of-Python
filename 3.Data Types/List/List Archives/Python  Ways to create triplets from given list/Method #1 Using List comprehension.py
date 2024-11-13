# Python code to create triplets from list of words.

# List of word initialization
list_of_words = ['I', 'am', 'Paras', 'Jain',
				'I', 'Study', 'DS', 'Algo']

# Using list comprehension
List = [list_of_words[i:i + 3]
		for i in range(len(list_of_words) - 2)]

# printing list
print(List)
