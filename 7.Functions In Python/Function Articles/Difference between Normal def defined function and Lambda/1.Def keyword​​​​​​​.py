# Define function to calculate cube root
# using def keyword

def calculate_cube_root(x):
	return x**(1/3)

# Call the def function to calculate cube
# root and print it
print(calculate_cube_root(27))

# Define function to check if language is present in
# language list using def keyword
languages = ['Sanskrut', 'English', 'French', 'German']

def check_language(x):
	if x in languages:
		return True
	return False

# Call the def function to check if keyword 'English'
# is present in the languages list and print it
print(check_language('English'))
