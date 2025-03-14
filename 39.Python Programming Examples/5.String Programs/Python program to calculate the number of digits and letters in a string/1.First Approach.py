# define all digits as string
all_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# define all letters
all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
			'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# given string
string = "geeks2for3geeks"

# intialized value
total_digits = 0
total_letters = 0

# iterate through all characters
for s in string:

	# if character found in all_digits then increment total_digits by one
	if s in all_digits:
		total_digits += 1

	# if character found in all_letters then increment total_letters by one
	elif s in all_letters:
		total_letters += 1

print("Total letters found :-", total_letters)
print("Total digits found :-", total_digits)
