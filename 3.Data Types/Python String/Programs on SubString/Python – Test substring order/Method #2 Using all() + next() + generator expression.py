# Python3 code to demonstrate working of
# Test substring order
# Using all() + next() + generator expression

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing substring
K = 'seek'

# concatenating required characters using next()
# all() used to test order
test_str = iter(test_str)
res = all(next((ele for ele in test_str if ele == chr), None) is not None for chr in K)

# printing result
print("Is substring in order : " + str(res))
