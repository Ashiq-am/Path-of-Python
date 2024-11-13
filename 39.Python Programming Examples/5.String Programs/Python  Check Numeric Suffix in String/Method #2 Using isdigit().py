# Python3 code to demonstrate working of
# Check Numeric Suffix in String
# Using isdigit()

# initializing string
test_str = "Geeks4321"

# printing original string
print("The original string is : " + str(test_str))

# Using isdigit()
# Check Numeric Suffix in String
res = test_str[-1].isdigit()

# printing result
print("Does string contain suffix number ? : " + str(res))
