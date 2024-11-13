# Python3 code to demonstrate working of
# Unpacking Integer Keys in Strings
# Using format() + * operator + values()

# initializing string
test_str = "First value is {} Second is {} Third {}"

# printing original string
print("The original string is : " + str(test_str))

# initializing dictionary
test_dict = {3: "Gfg", 4: "is", 9: "Best"}

# using format() for mapping required values
res = test_str.format(*test_dict.values())

# printing result
print("String after unpacking dictionary : " + str(res))
