# Python3 code to demonstrate working of
# Convert String to List of dictionaries
# Using json.loads + replace()

# initializing string
test_str = "[{'Gfg' : 3, 'Best' : 8}, {'Gfg' : 9, 'Best' : 9}]"

# printing original string
print("The original string is : " + str(test_str))

# eval() used to convert
res = list(eval(test_str))

# printing result
print("Converted list of dictionaries : " + str(res))
