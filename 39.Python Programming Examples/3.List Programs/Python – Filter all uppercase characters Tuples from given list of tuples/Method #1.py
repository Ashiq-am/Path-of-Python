# Python3 code to demonstrate working of
# Filter uppercase characters Tuples
# Using loop

# initializing list
test_list = [("GFG", "IS", "BEST"), ("GFg", "AVERAGE"), ("GFG",), ("Gfg", "CS")]

# printing original list
print("The original list is : " + str(test_list))

res_list = []
for sub in test_list:
    res = True
    for ele in sub:

        # checking for uppercase
        if not ele.isupper():
            res = False
            break
    if res:
        res_list.append(sub)

# printing results
print("Filtered Tuples : " + str(res_list))
