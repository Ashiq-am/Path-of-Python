import re

# Function to separate the numbers
# and alphabets from the given string
def separateNumbersAlphabets(str):
	numbers = re.findall(r'[0-9]+', str)
	alphabets = re.findall(r'[a-zA-Z]+', str)
	print(*numbers)
	print(*alphabets)

# Driver code
str = "adbv345hj43hvb42"
separateNumbersAlphabets(str)
