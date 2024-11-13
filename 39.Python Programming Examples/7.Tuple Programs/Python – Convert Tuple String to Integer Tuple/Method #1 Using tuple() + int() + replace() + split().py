# Python3 code to demonstrate working of
# Convert Tuple String to Integer Tuple
# Using tuple() + int() + replace() + split()

# initializing string
test_str = "(7, 8, 9)"

# printing original string
print("The original string is : " + test_str)

# Convert Tuple String to Integer Tuple
# Using tuple() + int() + replace() + split()
res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', '').split(', '))

# printing result
print("The tuple after conversion is : " + str(res))
