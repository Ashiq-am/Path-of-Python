# Python3 code to demonstrate working of
# Remove Duplicate Dictionaries characterized by Key
# Using loop

# initializing lists
test_list = [{"Gfg": 6, "is": 9, "best": 10},
             {"Gfg": 8, "is": 11, "best": 19},
             {"Gfg": 2, "is": 16, "best": 10},
             {"Gfg": 12, "is": 1, "best": 8},
             {"Gfg": 22, "is": 6, "best": 8}]

# printing original list
print("The original list : " + str(test_list))

# initializing Key
K = "best"

memo = set()
res = []
for sub in test_list:

    # testing for already present value
    if sub[K] not in memo:
        res.append(sub)

        # adding in memo if new value
        memo.add(sub[K])

# printing result
print("The filtered list : " + str(res))
