# Python3 code to demonstrate working of
# Convert String ranges to list
# Using sum() + list comprehension + enumerate() + split()

# initializing string
test_str = "1, 4-6, 8-10, 11"

# printing original string
print("The original string is : " + test_str)

# Convert String ranges to list
# Using sum() + list comprehension + enumerate() + split()
res = sum(((list(range(*[int(b) + c
		for c, b in enumerate(a.split('-'))]))
		if '-' in a else [int(a)]) for a in test_str.split(', ')), [])

# printing result
print("List after conversion from string : " + str(res))
