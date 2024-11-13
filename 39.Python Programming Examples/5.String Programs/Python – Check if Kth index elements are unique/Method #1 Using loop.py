# Python3 code to demonstrate working of
# Check if Kth index elements are unique
# Using loop

# initializing list
test_list = ["gfg", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

res = []
flag = True
for ele in test_list:

    # checking if element is repeated
    if ele[K] in res:
        flag = False
        break
    else:
        res.append(ele[K])

    # printing result
print("Is Kth index all unique : " + str(flag))
