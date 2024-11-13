# Python3 code to demonstrate working of
# Convert Tuple String to Integer Tuple
# Using eval()

# initializing string
test_str = "(7, 8, 9)"

# printing original string
print("The original string is : " + test_str)

# Convert Tuple String to Integer Tuple
# Using eval()
res = eval(test_str)

# printing result
print("The tuple after conversion is : " + str(res))
