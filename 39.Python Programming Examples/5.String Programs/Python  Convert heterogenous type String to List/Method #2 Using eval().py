# Python3 code to demonstrate working of
# Convert String of Heterogenous types to List
# using eval()

# initializing string
test_str = "'gfg', 'is', True, 'best', False, 1, 2"

# printing original string
print("The original string is : " + test_str)

# Convert String of Heterogenous types to List
# using eval()
res = list(eval(test_str))

# printing result
print("List after conversion from string : " + str(res))
