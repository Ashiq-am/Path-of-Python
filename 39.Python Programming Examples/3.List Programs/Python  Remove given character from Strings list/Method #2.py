# Python3 code to demonstrate working of
# Remove character from Strings list
# using list comprehension + replace()

# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# initialize character
char = 's'

# Remove character from Strings list
# using list comprehension + replace()
res = [ele.replace(char, '') for ele in test_list]

# printing result
print("The list after removal of character : " + str(res))
