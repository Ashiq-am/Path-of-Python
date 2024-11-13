# Python3 code to demonstrate working of
# Replace vowels by next vowel
# Using list comprehension + zip()

# initializing string
test_str = 'geekforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# constructing dictionary using zip()
vow = 'a e i o u'.split()
temp = dict(zip(vow, vow[1:] + [vow[0]]))

# list comprehension to perform replacement
res = "".join([temp.get(ele, ele) for ele in test_str])

# printing result
print("The replaced string : " + str(res))
