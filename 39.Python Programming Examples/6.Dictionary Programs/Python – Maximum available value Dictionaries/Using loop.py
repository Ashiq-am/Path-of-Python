# Python3 code to demonstrate working of
# Maximum available value Dictionaries
# Using loop

# initializing lists
test_list = [{"Gfg": 6, "is": 9, "best": 10},
             {"Gfg": 8, "is": 11, "best": 19},
             {"Gfg": 2, "is": 16, "best": 10},
             {"Gfg": 12, "is": 1, "best": 8},
             {"Gfg": 22, "is": 6, "best": 8}]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = "best"

# initializing list
arg_list = [10, 7, 6, 12]

# extracting value to find from dictionary
# corresponding to key
max_ele = 0
for sub in test_list:
    if sub[K] in arg_list:
        # maximum of all possible present for a key
        max_ele = max(sub[K], max_ele)

# extracting dictionary with maximum and present value of key
res = [sub for sub in test_list if sub[K] == max_ele]

# printing result
print("The extracted dictionaries : " + str(res))
