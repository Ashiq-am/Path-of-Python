# Python code to filter element from list
# based on another list of string.

# List Initialization
Input = ['key', 'keys', 'keyword', 'keychain', 'keynote']
Input_string = ['home/key/1.pdf',
		'home/keys/2.pdf',
		'home/keyword/3.pdf',
		'home/keychain/4.pdf',
		'home/Desktop/5.pdf',
		'home/keynote/6.pdf']

# Using list comprehension
Output = [b for b in Input_string if
		all(a not in b for a in Input)]

# Printing
print("List of keywords are:", Input)
print("Given list:", Input_string)
print("filtered list is :", Output)
