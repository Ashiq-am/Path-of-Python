def count_vowels_recursive(s):
	# Base case: empty string
	if not s:
		return 0
	# Check if the first character is a vowel
	elif s[0].lower() in 'aeiou':
		return 1 + count_vowels_recursive(s[1:])
	else:
		return count_vowels_recursive(s[1:])
