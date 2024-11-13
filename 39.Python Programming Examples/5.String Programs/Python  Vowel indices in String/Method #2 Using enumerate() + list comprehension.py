# Python3 code to demonstrate working of
# Vowel indices in String
# Using list comprehension + enumerate()

# initializing string
test_str = "geeksforgeeks"

# printing original string
print("The original string is : " + test_str)

# Vowel indices in String
# Using list comprehension + enumerate()
res = [idx for idx, ele in enumerate(test_str) if ele in "aeiou"]

# printing result
print("The vowel indices are : " + str(res))
