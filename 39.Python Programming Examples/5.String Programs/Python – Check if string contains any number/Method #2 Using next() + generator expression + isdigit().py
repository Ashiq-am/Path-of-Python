# Python3 code to demonstrate working of
# Check if string contains any number
# Using isdigit() + next() + generator expression

# initializing string
test_str = 'geeks4geeks'

# printing original string
print("The original string is : " + str(test_str))

# next() checking for each element, reaches end, if no element found as digit
res = True if next((chr for chr in test_str if chr.isdigit()), None) else False

# printing result
print("Does string contain any digit ? : " + str(res))
