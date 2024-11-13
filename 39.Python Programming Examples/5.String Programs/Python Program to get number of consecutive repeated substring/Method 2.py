# Python3 code to demonstrate working of
# Number of repeated substrings in consecution
# Using findall() + regex + len()
import re

# initializing string
test_str = 'geeksgeeksaregeeksgeeksgeeksforallgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 'geeks'
n = len(K)

# getting regex
regx = re.compile(f'((?:{K})+)')

# getting repeats counts
# findall finding all substring joined repetitions
res = [len(occ) // n for occ in regx.findall(test_str)]

# printing result
print("String repetitions : " + str(res))
