# Python3 code to demonstrate working of
# Concatenate Ranged Values in String list
# Using loop

# initializing list
test_list = ["abGFGcs", "cdforef", "asalloi"]

# printing original list
print("The original list : " + str(test_list))

# initializing range
i, j = 2, 5

res = ''
for ele in test_list:
    # Concatenating required range
    res += ele[i: j]

# printing result
print("The Concatenated String : " + str(res))
