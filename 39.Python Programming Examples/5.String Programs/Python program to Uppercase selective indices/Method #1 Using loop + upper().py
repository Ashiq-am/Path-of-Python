# Python3 code to demonstrate working of
# Uppercase selective indices
# Using loop + upper()

# initializing string
test_str = 'geeksgeeksisbestforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing indices list
idx_list = [5, 7, 3, 2, 6, 9]

res = ''
for idx in range(0, len(test_str)):

    # checking for index list for uppercase
    if idx in idx_list:
        res += test_str[idx].upper()
    else:
        res += test_str[idx]

    # printing result
print("Transformed String : " + str(res))
