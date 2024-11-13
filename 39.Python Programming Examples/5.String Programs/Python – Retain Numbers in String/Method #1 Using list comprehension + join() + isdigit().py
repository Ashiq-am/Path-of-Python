# Python3 code to demonstrate working of
# Retain Numbers in String
# Using list comprehension + join() + isdigit()

# initializing string
test_str = 'G4g is No. 1 for Geeks 7'

# printing original string
print("The original string is : " + str(test_str))

# Retain Numbers in String
# Using list comprehension + join() + isdigit()
res = "".join([ele for ele in test_str if ele.isdigit()])

# printing result
print("String after integer retention : " + str(res))
