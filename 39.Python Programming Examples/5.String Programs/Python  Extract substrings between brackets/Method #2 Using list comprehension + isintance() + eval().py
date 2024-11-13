# Python3 code to demonstrate working of
# Extract substrings between brackets
# Using list comprehension + eval() + isinstance()

# initializing string
test_str = "[(234, ), 4, (432, )]"

# printing original string
print("The original string is : " + test_str)

# Extract substrings between brackets
# Using list comprehension + eval() + isinstance()
res = [str(idx) for idx in eval(test_str) if isinstance(idx, tuple)]

# printing result
print("The element between brackets : " + str(res))
