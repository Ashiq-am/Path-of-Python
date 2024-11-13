# Python3 code to demonstrate working of
# Conditional Uppercase by size
# Using upper() + loop

# initializing list
test_list = ["Gfg", "is", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

res = []
for ele in test_list:

    # check for size
    if len(ele) > K:
        res.append(ele.upper())
    else:
        res.append(ele)

    # printing result
print("Modified Strings : " + str(res))
