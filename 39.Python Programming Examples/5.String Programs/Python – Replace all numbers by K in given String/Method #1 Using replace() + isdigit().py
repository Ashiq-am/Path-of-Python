# Python3 code to demonstrate working of
# Replace numbers by K in String
# Using replace() + isdigit()

# initializing string
test_str = 'G4G is 4 all No. 1 Geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = '@'

# loop for all characters
for ele in test_str:
    if ele.isdigit():
        test_str = test_str.replace(ele, K)

    # printing result
print("The resultant string : " + str(test_str))
