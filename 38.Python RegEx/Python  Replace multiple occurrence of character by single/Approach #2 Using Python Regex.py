import re

# Function to replace multiple occurrences
# of a character by a single character
def replace(string, char):
	pattern = char + '{2,}'
	string = re.sub(pattern, char, string)
	return string

# Driver code
string = 'Geeksforgeeks'
char = 'e'
print(replace(string, char))
