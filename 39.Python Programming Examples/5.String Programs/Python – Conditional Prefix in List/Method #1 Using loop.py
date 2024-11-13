# Python3 code to demonstrate working of
# Conditional Prefix in List
# Using loop

# initializing list
test_list = [45, 53, 76, 86, 3, 49]

# printing original list
print("The original list : " + str(test_list))

# initializing pref 1
pref_1 = "LOW-"

# initializing pref 2
pref_2 = "HIGH-"

res = []
for ele in test_list:

    # appending prefix on greater than 50 check
    if ele >= 50:
        res.append(pref_2 + str(ele))
    else:
        res.append(pref_1 + str(ele))

    # printing result
print("The prefixed elements : " + str(res))
