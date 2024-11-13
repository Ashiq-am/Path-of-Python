# Python3 code to demonstrate working of
# Replace duplicate Occurrence in String
# Using keys() + index() + list comprehension

# initializing string
test_str = 'Gfg is best . Gfg also has Classes now. Classes help understand better . '

# printing original string
print("The original string is : " + str(test_str))

# initializing replace mapping
repl_dict = {'Gfg' : 'It', 'Classes' : 'They' }

# Replace duplicate Occurrence in String
# Using keys() + index() + list comprehension
test_list = test_str.split(' ')
res = ' '.join([repl_dict.get(val) if val in repl_dict.keys() and test_list.index(val) != idx
								else val for idx, val in enumerate(test_list)])

# printing result
print("The string after replacing : " + str(res))
