# Python3 code to demonstrate working of
# Reverse Incremental String Slicing
# Using list comprehension + list slicing

# initializing string
test_str = "geeks"

# printing original string
print("The original string is : " + test_str)

# Reverse Incremental String Slicing
# Using list comprehension + list slicing
res = [test_str[-1 : idx : -1] for idx in range(-2, -2 - len(test_str), -1)]

# printing result
print("The incremental reverse strings : " + str(res))
