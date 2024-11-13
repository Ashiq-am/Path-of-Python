# Python3 code to demonstrate working of
# Convert K delim Strings to Integer Tuple List
# Using map() + split() + list comprehension

# initializing list
test_list = ["1-2", "3-4-8-9", "4-10-4"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = "-"

# extension logic using map()
# int() is used for conversion
res = [tuple(map(int, sub.split(K))) for sub in test_list]

# printing result
print("The converted tuple list : " + str(res))
