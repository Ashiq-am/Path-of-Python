# Python3 code to demonstrate working of
# Remove character from Strings list
# using loop + replace() + enumerate()

# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# initialize character
char = 's'

# Remove character from Strings list
# using loop + replace() + enumerate()
for idx, ele in enumerate(test_list):
		test_list[idx] = ele.replace(char, '')

# printing result
print("The list after removal of character : " + str(test_list))
