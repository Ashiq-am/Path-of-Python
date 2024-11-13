# Python3 code to demonstrate working of
# Get Nth word in String
# using split()

# initializing string
test_str = "GFG is for Geeks"

# printing original string
print("The original string is : " + test_str)

# initializing N
N = 3

# Get Nth word in String
# using split()
res = test_str.split(' ')[N-1]

# printing result
print("The Nth word in String : " + res)
