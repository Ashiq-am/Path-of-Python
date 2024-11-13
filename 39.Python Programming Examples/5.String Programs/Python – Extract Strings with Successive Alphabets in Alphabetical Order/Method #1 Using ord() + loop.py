# Python3 code to demonstrate working of
# Extract Strings with successive Alphabets
# Using ord() + loop

# initializing string list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

res = []
for sub in test_list:

    # iterating for string
    for idx in range(len(sub) - 1):

        # checking for alphabetic consecution
        if ord(sub[idx]) == ord(sub[idx + 1]) - 1:
            res.append(sub)
            break

# printing result
print("Strings with alphabetic consecution : " + str(res))
