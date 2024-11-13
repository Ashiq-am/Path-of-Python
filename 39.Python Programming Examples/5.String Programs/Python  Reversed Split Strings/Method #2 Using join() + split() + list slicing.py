# Python3 code to demonstrate
# Reverse string split
# using join() + split() + list slicing

# initializing string
test_string = "Gfg is best"

# printing original string
print("The original string : " + str(test_string))

# using join() + split() + list slicing
# Reverse string split
res = ', '.join(test_string.split()[::-1])

# print result
print("The string after reverse split : " + str(res))
