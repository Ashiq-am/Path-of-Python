# Python3 code to demonstrate working of
# Alternate K Length characters
# Using loop + slicing

# initializing string
test_str = 'geeksgeeksisbestforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 4

res = ''

# skipping k * 2 for altering effect
for idx in range(0, len(test_str), K * 2):
    # concatenating K chars
    res += test_str[idx: idx + K]

# printing result
print("Transformed String : " + str(res))
