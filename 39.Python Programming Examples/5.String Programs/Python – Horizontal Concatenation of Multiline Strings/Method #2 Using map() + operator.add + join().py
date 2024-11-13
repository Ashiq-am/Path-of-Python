# Python3 code to demonstrate working of
# Horizontal Concatenation of Multiline Strings
# Using map() + operator.add + join()
from operator import add

# initializing strings
test_str1 = ''' 
geeks 4 
geeks'''
test_str2 = ''' 
is 
best'''

# printing original strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

# using add to concat, map() to concat each lines zipped
res = '\n'.join(map(add, test_str1.split('\n'), test_str2.split('\n')))

# printing result
print("After String Horizontal Concatenation : " + str(res))
