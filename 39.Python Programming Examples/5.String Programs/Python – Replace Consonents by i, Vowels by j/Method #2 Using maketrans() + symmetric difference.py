# Python3 code to demonstrate working of
# Replace Consonents by i, Vowels by j
# Using maketrans() + symmetric difference
import string

# initializing strings
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing i, j
i, j = "V", "C"

# extracting voweks and consonents
Vows = 'aeiouAEIOU'

# using sym. diff to get consonents
Cons = ''.join(set(string.ascii_letters).difference(set(Vows)))

# initializing translation
translation = str.maketrans(Vows + Cons, i * len(Vows) + j * len(Cons))

res = test_str.translate(translation)

# printing result
print("The string after required replacement : " + str(res))
