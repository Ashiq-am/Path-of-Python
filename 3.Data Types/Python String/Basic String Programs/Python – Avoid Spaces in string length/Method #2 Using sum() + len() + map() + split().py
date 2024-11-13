# Python3 code to demonstrate working of
# Avoid Spaces in Characters Frequency
# Using sum() + len() + map() + split()

# initializing string
test_str = 'geeksforgeeks 33 is best'

# printing original string
print("The original string is : " + str(test_str))

# len() finds individual word Frequency
# sum() extracts final Frequency
res = sum(map(len, test_str.split()))

# printing result
print("The Characters Frequency avoiding spaces : " + str(res))
