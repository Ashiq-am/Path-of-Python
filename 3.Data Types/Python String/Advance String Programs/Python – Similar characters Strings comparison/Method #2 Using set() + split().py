# Python3 code to demonstrate working of
# Similar characters Strings comparison
# Using set() + split()

# initializing strings
test_str1 = 'e:k:s:g'
test_str2 = 'g:e:k:s'

# printing original strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

# initializing delim
delim = ':'

# == operator is used for comparison
# removes duplicates and compares
res = set(test_str1.split(':')) == set(test_str2.split(':'))

# printing result
print("Are strings similar : " + str(res))
