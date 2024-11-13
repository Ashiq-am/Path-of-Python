# Python3 code to demonstrate working of
# Replace K with Multiple values
# Using loop + replace()

# initializing strings
test_str = '_ is _ . It is recommended for _'

# printing original string
print("The original string is : " + str(test_str))

# initializing repl_char
repl_char = '_'

# initializing repl_list
repl_list = ['Gfg', 'Best', 'CS']

# Replace K with Multiple values
# Using loop + replace()
for ele in repl_list:
	test_str = test_str.replace(repl_char, ele, 1)

# printing result
print("String after replacement : " + str(test_str))
