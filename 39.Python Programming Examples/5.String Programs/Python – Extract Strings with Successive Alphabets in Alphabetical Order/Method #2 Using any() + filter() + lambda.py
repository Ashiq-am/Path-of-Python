# Python3 code to demonstrate working of
# Extract Strings with successive Alphabets
# Using any() + filter() + lambda

# initializing string list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

# filtering using filter, and checking for any substring using any()
res = list(filter(lambda sub: any(ord(sub[idx]) == ord(
	sub[idx + 1]) - 1 for idx in range(len(sub) - 1)), test_list))

# printing result
print("Strings with alphabetic consecution : " + str(res))
