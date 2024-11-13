# Python3 code to demonstrate working of
# Convert Stream of numbers to list
# Using list() + split()

# initializing string
test_str = "10 12 3 54 6 777 443"

# printing original string
print("The original string is : " + test_str)

# Using list() + split()
# Convert Stream of numbers to list
res = list(test_str.split())

# printing result
print("The list of stream of numbers : " + str(res))
