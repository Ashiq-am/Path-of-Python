# Python3 code to demonstrate working of
# Incremental Size Chunks from Strings
# Using loop + slicing

# initializing string
test_str = 'geekforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

res = []
idx = 1
while True:
    if len(test_str) > idx:

        # chunking
        res.append(test_str[0: idx])
        test_str = test_str[idx:]
        idx += 1
    else:
        res.append(test_str)
        break

# printing result
print("The Incremental sized Chunks : " + str(res))
