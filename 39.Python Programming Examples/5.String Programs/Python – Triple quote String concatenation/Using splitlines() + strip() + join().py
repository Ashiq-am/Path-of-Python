# Python3 code to demonstrate working of
# Triple quote String concatenation
# Using splitlines() + join() + strip()

# initializing strings
test_str1 = """gfg 
is"""
test_str2 = """best 
for geeks 
"""

# printing original strings
print("The original string 1 is : " + test_str1)
print("The original string 2 is : " + test_str2)

# Triple quote String concatenation
# Using splitlines() + join() + strip()
test_str1 = test_str1.splitlines()
test_str2 = test_str2.splitlines()
res = []

for i, j in zip(test_str1, test_str2):
	res.append(" " + i.strip() + " " + j.strip())
res = '\n'.join(res)

# printing result
print("String after concatenation : " + str(res))
