# Python3 code to demonstrate working of
# Vowel indices in String
# Using loop

# initializing string
test_str = "geeksforgeeks"

# printing original string
print("The original string is : " + test_str)

# Vowel indices in String
# Using loop
res = []
for ele in range(len(test_str)):
    if test_str[ele] in "aeiou":
        res.append(ele)

# printing result
print("The vowel indices are : " + str(res))
