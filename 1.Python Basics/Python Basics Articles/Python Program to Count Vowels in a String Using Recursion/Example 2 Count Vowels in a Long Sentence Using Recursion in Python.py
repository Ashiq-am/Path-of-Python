def count_vowels(string):
	# Base case: if the string is empty, return 0
	if not string:
		return 0
	# Check if the first character is a vowel
	if string[0].lower() in 'aeiou':
		# If it is, add 1 and recurse on the rest of the string
		return 1 + count_vowels(string[1:])
	else:
		# If it's not a vowel, just recurse on the rest of the string
		return count_vowels(string[1:])


# Example usage:
string = "Hello World, This is GeeksforGeeks World!"
print("Number of vowels:", count_vowels(string))
