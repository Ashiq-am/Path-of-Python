# Python3 code to demonstrate working of
# Convert String of Heterogenous types to List
# using list comprehension + split() + strip()

# initializing string
test_str = "'gfg', 'is', True, 'best', False"

# printing original string
print("The original string is : " + test_str)

# Convert String of Heterogenous types to List
# using list comprehension + split() + strip()
res = [ele.strip() if ele.strip().startswith("'") else ele == 'True'
	for ele in test_str.split(', ')]

# printing result
print("List after conversion from string : " + str(res))
