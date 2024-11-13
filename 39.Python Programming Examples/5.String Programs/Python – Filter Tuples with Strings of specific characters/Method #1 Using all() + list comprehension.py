# Python3 code to demonstrate working of
# Filter Tuples with Strings of specific characters
# Using all() + list comprehension

# initializing lists
test_list = [('gfg', 'best'), ('gfg', 'good'), ('fest', 'gfg')]

# printing original lists
print("The original list is : " + str(test_list))

# initializing char_str
char_str = 'gfestb'

# nested all(), to check for all characters in list,
# and for all strings in tuples
res = [sub for sub in test_list if all(
	all(el in char_str for el in ele) for ele in sub)]

# printing result
print("The filtered tuples : " + str(res))
