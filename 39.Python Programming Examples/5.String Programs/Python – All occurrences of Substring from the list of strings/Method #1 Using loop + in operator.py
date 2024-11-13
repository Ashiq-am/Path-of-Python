# Python3 code to demonstrate working of
# Strings with all Substring Matches
# Using loop + in operator

# initializing list
test_list = ["gfg is best", "gfg is good for CS",
             "gfg is recommended for CS"]

# printing original list
print("The original list is : " + str(test_list))

# initializing Substring List
subs_list = ["gfg", "CS"]

res = []
for sub in test_list:
    flag = 0
    for ele in subs_list:

        # checking for non existance of
        # any string
        if ele not in sub:
            flag = 1
            break
    if flag == 0:
        res.append(sub)

    # printing result
print("The extracted values : " + str(res))
