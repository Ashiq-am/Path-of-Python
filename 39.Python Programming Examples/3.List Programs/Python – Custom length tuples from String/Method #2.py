# Python3 code to demonstrate working of
# Custom length tuples from String
# Using map() + int + tuple() + list comprehension + split()

# initializing string
test_str = '4 6 7, 1 2, 3, 4 6 8 8'

# printing original string
print("The original string is : " + str(test_str))

# split() used to split on delimiter and
# using map() to extend logic of element casting
res = [tuple(map(int, sub.split())) for sub in test_str.split(", ")]

# printing result
print("The constructed custom length tuples : " + str(res))
