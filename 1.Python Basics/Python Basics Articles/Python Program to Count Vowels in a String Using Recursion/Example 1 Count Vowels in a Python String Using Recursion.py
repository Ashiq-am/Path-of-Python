def count_vowels(string):
	# Base case: if the string is empty, return 0
	if not string:
		return 0
	# Check if the first character is a vowel
	if string[0].lower() in 'aeiou':
		return 1 + count_vowels(string[1:])
	else:
		return count_vowels(string[1:])


# Example usage:
string = "Geeksforgeeks"
print("Number of vowels:", count_vowels(string))
