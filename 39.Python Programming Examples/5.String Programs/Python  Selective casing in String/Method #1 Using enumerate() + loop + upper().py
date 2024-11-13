# Python3 code to demonstrate working of
# Selective casing in String
# using loop + upper() + enumerate()

# initialize string
test_str = 'gfg is best'

# printing original string
print("The original string : " + str(test_str))

# initialize change case list
chg_list = ['g', 'f', 's']

# Selective casing in String
# using loop + upper() + enumerate()
res = list(test_str)
for idx, char in enumerate(res):
	if char in chg_list:
		res[idx] = char.upper()

# printing result
print("String after Selective casing : " + str(''.join(res)))
