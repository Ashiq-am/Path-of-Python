# Python3 code to demonstrate working of
# Replace K with Multiple values
# Using split() + join() + zip()

# initializing strings
test_str = '_ is _ . It is recommended for _'

# printing original string
print("The original string is : " + str(test_str))

# initializing repl_char
repl_char = '_'

# initializing repl_list
repl_list = ['Gfg', 'Best', 'CS']

# Replace K with Multiple values
# Using split() + join() + zip()
test_list = test_str.split(repl_char)
temp = zip(test_list, repl_list)
res = ''.join([ele for sub in temp for ele in sub])

# printing result
print("String after replacement : " + str(res))
