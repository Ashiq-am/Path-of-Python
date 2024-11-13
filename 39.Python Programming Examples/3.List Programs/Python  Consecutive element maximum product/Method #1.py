# Python3 code to demonstrate
# Consecutive element maximum product
# using zip() + max() + list comprehension

# initializing string
test_string = '2312231223124565128998'

# printing original string
print("The original string : " + str(test_string))

# using zip() + max() + list comprehension
# Consecutive element maximum product
test_string = list(test_string)
res = max(int(a) * int(b) for a, b in zip(test_string, test_string[1:]))

# print result
print("The maximum consecutive product is : " + str(res))
