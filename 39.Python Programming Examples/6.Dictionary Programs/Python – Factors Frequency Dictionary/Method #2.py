# Python3 code to demonstrate working of
# Factors Frequency Dictionary
# Using sum() + loop

# initializing list
test_list = [2, 4, 6, 8, 3, 9, 12, 15, 16, 18]

# printing original list
print("The original list : " + str(test_list))

res = dict()
for idx in range(1, max(test_list)):
    # using sum() instead of loop for sum computation
    res[idx] = sum(key % idx == 0 for key in test_list)

# printing result
print("The constructed dictionary : " + str(res))
