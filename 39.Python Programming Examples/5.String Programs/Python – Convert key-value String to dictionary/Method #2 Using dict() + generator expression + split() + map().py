# Python3 code to demonstrate working of
# Convert key-value String to dictionary
# Using dict() + generator expression + split() + map()

# initializing string
test_str = 'gfg:1, is:2, best:3'

# printing original string
print("The original string is : " + str(test_str))

# Convert key-value String to dictionary
# Using dict() + generator expression + split() + map()
res = dict(map(str.strip, sub.split(':', 1)) for sub in test_str.split(', ') if ':' in sub)

# printing result
print("The converted dictionary is : " + str(res))
