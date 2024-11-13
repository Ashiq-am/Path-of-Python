def is_string_empty(my_string):
	return my_string is None or len(my_string.strip()) == 0

my_string1 = "opkr"
my_string2 = ""

if is_string_empty(my_string1):
	print("String 1 is empty.")
else:
	print("String 1 is not empty.")

if is_string_empty(my_string2):
	print("String 2 is empty.")
else:
	print("String 2 is not empty.")
