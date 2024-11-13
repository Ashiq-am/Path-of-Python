# Python3 code to demonstrate working of
# Uppercase Indices
# Using list comprehension + range() + isupper()

# initializing string
test_str = 'GeeKsFoRGEEks'

# printing original string
print("The original string is : " + str(test_str))

# Uppercase check using isupper()
res = [idx for idx in range(len(test_str)) if test_str[idx].isupper()]

# printing result
print("Uppercase elements indices : " + str(res))
