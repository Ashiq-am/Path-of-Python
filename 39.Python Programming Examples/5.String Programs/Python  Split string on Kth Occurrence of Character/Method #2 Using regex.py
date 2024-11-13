# Python3 code to demonstrate working of
# Split string on Kth Occurrence of Character
# Using regex
import re

# initializing string
test_str = "Geeks_for_Geeks_is_best"

# split char
splt_char = "_"

# initializing K
K = 3

# printing original string
print("The original string is : " + str(test_str))

# Using regex
# Split string on Kth Occurrence of Character
temp = [x.start() for x in re.finditer(splt_char, test_str)]
res1 = test_str[0:temp[K - 1]]
res2 = test_str[temp[K - 1] + 1:]
res = (res1 + " " + res2).split(" ")

# printing result
print("Is list after Kth split is : " + str(res))
