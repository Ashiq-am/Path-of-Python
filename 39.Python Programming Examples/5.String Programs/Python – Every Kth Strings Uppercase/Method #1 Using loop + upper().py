# Python3 code to demonstrate working of
# Every Kth Strings Uppercase
# Using loop + upper()

# initializing list
test_list = ["gfg", "is", "best", "for", "geeks", "and", "CS"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

res = []
for idx in range(len(test_list)):

    # checking for Kth index
    if idx % K == 0:
        res.append(test_list[idx].upper())
    else:
        res.append(test_list[idx])

    # printing result
print("The resultant String list : " + str(res))
