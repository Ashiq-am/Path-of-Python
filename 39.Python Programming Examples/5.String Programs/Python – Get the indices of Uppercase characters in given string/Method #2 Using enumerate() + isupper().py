# Python3 code to demonstrate working of
# Uppercase Indices
# Using enumerate() + isupper()

# initializing string
test_str = 'GeeKsFoRGEEks'

# printing original string
print("The original string is : " + str(test_str))

# Uppercase check using isupper()
# enumerate() gets indices
res = [idx for idx, chr in enumerate(test_str) if chr.isupper()]

# printing result
print("Uppercase elements indices : " + str(res))
