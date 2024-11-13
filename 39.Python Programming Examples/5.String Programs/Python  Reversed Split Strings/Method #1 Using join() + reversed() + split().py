# Python3 code to demonstrate
# Reverse string split
# using join() + reversed() + split()

# initializing string
test_string = "Gfg is best"

# printing original string
print("The original string : " + str(test_string))

# using join() + reversed() + split()
# Reverse string split
res = ", ".join(reversed(test_string.split(" ")))

# print result
print("The string after reverse split : " + str(res))
