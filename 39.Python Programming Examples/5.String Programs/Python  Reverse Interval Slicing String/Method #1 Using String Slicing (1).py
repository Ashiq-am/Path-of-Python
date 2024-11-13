# Python3 code to demonstrate working of
# Reverse Interval Slicing String
# Using String Slicing 1

# initializing string
test_str = "geeksforgeeks"

# printing original string
print("The original string is : " + test_str)

# initializing Interval
K = 2

# Reverse Interval Slicing String
# Using String Slicing 1
res = test_str[::K][::-1]

# printing result
print("The reverse Interval Slice : " + str(res))
