# Python3 code to demonstrate working of
# Group Strings by K length Suffix
# Using try/except + loop

# initializing list
test_list = ["food", "peak", "geek",
             "good", "weak", "sneek"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

res = {}
for ele in test_list:

    # extracting suffix
    suff = ele[-K:]

    # appending if key found, else creating new one
    try:
        res[suff].append(ele)
    except:
        res[suff] = [ele]

    # printing result
print("The grouped suffix Strings : " + str(res))
