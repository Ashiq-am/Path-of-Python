# Python3 code to demonstrate working of
# Print Alphabets till N
# Using string.ascii_lowercase + slicing
import string

# initialize N
N = 20

# printing N
print("Number of elements required : " + str(N))

# Print Alphabets till N
# Using string.ascii_lowercase + slicing
res = string.ascii_lowercase[:N]

# printing result
print("Alphabets till N are : " + str(res))
