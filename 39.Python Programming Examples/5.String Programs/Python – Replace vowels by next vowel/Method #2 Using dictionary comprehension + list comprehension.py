# Python3 code to demonstrate working of
# Replace vowels by next vowel
# Using list comprehension + dictionary comprehension

# initializing string
test_str = 'geekforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# constructing dictionary using dictionary comprehension
vow = "aeiou"
temp = {vow[idx] : vow[(idx + 1) % len(vow)] for idx in range(len(vow))}

# using get() to map elements to dictionary and join to convert
res = "".join([temp.get(ele, ele) for ele in test_str])

# printing result
print("The replaced string : " + str(res))
