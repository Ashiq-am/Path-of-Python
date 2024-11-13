# Python3 code to demonstrate working of
# Filter String Tuples if String lengths equals K
# Using loop

# initializing list
test_list = [("ABC", "Gfg", "CS1"), ("Gfg", "Best"), ("Gfg", "WoW")]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

res_list = []
for sub in test_list:
    res = True
    for ele in sub:

        # check using len() the lengths
        if len(ele) != K:
            res = False
            break
    if res:
        res_list.append(sub)

# printing result
print("The filtered tuples : " + str(res_list))
