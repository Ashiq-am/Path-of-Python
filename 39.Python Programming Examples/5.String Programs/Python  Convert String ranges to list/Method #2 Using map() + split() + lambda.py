# Python2 code to demonstrate working of
# Convert String ranges to list
# Using map() + lambda + split()

# initializing string
test_str = "1, 4-6, 8-10, 11"

# printing original string
print("The original string is : " + test_str)

# Convert String ranges to list
# Using map() + lambda + split()
temp = [(lambda sub: range(sub[0], sub[-1] + 1))(map(int, ele.split('-')))\
		for ele in test_str.split(', ')]

res = [b for a in temp for b in a]

# printing result
print("List after conversion from string : " + str(res))
