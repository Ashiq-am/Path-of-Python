# Python3 code to demonstrate working of
# Reverse String except punctuations
# Using groupby() + isalnum() [ for substing specific reversal ]
from itertools import groupby

# initializing string
test_str = 'geeks# for&%% gee)ks'

# printing original string
print("The original string is : " + str(test_str))

res = ''

# grouping all sections
for ele, sub in groupby(test_str, str.isalnum):
    sub = list(sub)

    # reversal on alphanumeric occurrence
    if ele:
        sub = sub[::-1]

    # joining all subparts
    res += ''.join(sub)

# printing result
print("The Reversed String ignoring punctuation [substring] : " + str(res))
