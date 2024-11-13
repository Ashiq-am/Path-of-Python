# Python3 code to demonstrate working of
# Phrase extraction in String
# Using list comprehension + enumerate() + list slicing

# initializing string
test_str = 'Geeksforgeeks is best for geeks and CS'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 2

# Phrase extraction in String
# Using list comprehension + enumerate() + list slicing
temp = [idx for idx, ele in enumerate(test_str) if ele == ' ']
res = test_str[temp[K - 1]: temp[-(K - 1)]].strip()

# printing result
print("String after phrase removal : " + str(res))
