# Python3 code to demonstrate working of
# Remove similar index elements in Strings
# Using list comprehension

# initializing strings
test_str1 = 'geeks'
test_str2 = 'beaks'

# printing original strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

# one-liner to solve problem
res = ["".join(mastr) for mastr
	in zip(*[(a, b) for a, b in zip(test_str1, test_str2) if a != b])]

# printing result
print("Modified String 1 : " + str(res[0]))
print("Modified String 2 : " + str(res[1]))
