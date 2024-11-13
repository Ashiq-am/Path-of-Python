# Python3 code to demonstrate working of
# Convert String to tuple list
# using eval()

# initializing string
test_str = "(1, 3, 4), (5, 6, 4), (1, 3, 6)"

# printing original string
print("The original string is : " + test_str)

# Convert String to tuple list
# using eval()
res = list(eval(test_str))

# printing result
print("List after conversion from string : " + str(res))
