# Python3 code to demonstrate working of
# Cartesian product of string elements
# Using split() + list comprehension

# initializing strings
test_str1 = "gfg, is, best"
test_str2 = "for, all, geeks"

# printing original strings
print("The original string 1 is : " + test_str1)
print("The original string 2 is : " + test_str2)

# Cartesian product of string elements
# Using split() + list comprehension
res = [sub1 + sub2 for sub1 in test_str1.split(", ") for sub2 in test_str2.split(", ")]

# printing result
print("Cartesian product list : " + str(res))
