# Python3 code to demonstrate working of
# Uppercase custom characters
# Using upper() + loop

# initializing string
test_str = 'gfg is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing upperlist
upper_list = ['g', 'e', 'b', 'k']

res = ''
for ele in test_str:

    # checking for presence in upper list
    if ele in upper_list:
        res += ele.upper()
    else:
        res += ele

    # printing result
print("String after reconstruction : " + str(res))
