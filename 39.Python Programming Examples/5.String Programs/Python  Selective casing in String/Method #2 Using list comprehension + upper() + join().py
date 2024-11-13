# Python3 code to demonstrate working of
# Selective casing in String
# using list comprehension + upper() + join()

# initialize string
test_str = 'gfg is best'

# printing original string
print("The original string : " + str(test_str))

# initialize change case list
chg_list = ['g', 'f', 's']

# Selective casing in String
# using list comprehension + upper() + join()
res = ''.join([char.upper() if char in chg_list
				else char for char in test_str])

# printing result
print("String after Selective casing : " + str(''.join(res)))
