# Python3 code to demonstrate working of
# Custom length tuples from String
# Using int() + tuple() + split() + list comprehension

# initializing string
test_str = '4 6 7, 1 2, 3, 4 6 8 8'

# printing original string
print("The original string is : " + str(test_str))

# split() used to split on delimiter and
# type casted to int followed by tuple casting
test_str = test_str.split(', ')
res = [tuple(int(ele) for ele in sub.split()) for sub in test_str]

# printing result
print("The constructed custom length tuples : " + str(res))
