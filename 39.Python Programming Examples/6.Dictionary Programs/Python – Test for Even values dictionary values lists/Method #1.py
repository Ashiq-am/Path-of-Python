# Python3 code to demonstrate working of
# Test for Even values dictionary values lists
# Using loop

# initializing dictionary
test_dict = {"Gfg": [6, 7, 3],
             "is": [8, 10, 12, 16],
             "Best": [10, 16, 14, 6]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

res = dict()
for sub in test_dict:
    flag = 1

    # checking for even elements
    for ele in test_dict[sub]:
        if ele % 2 != 0:
            flag = 0
            break
    # adding True if all Even elements
    res[sub] = True if flag else False

# printing result
print("The computed dictionary : " + str(res))
