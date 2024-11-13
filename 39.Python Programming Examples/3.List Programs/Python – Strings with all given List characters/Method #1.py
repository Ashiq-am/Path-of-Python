# Python3 code to demonstrate working of
# Strings with all List characters
# Using loop

# initializing list
test_list = ["Geeks", "Gfg", "Geeksforgeeks", "free"]

# printing original list
print("The original list is : " + str(test_list))

# initializing char_list
chr_list = ['g', 'f']

res_list = []
for sub in test_list:
    res = True
    for ele in chr_list:

        # check if any element is not present
        if ele not in sub:
            res = False
            break
    if res:
        res_list.append(sub)

# printing results
print("Filtered Strings : " + str(res_list))
