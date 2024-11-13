# Python3 code to demonstrate working of
# Remove K value items from dictionary nestings
# Using dictionary comprehension + loop

# initializing list
test_list = [{"Gfg": {"a": 5, "b": 8, "c": 9}},
             {"is": {"f": 8, "j": 8, "k": 10}},
             {"Best": {"i": 16}}]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 8

res = list()

for sub in test_list:
    for key, val in sub.items():

        # iterating for 1st nesting only
        for key1, val1 in val.items():
            if val1 != K:
                res.append({key1: val1})

# printing result
print("The dictionary after value removal : " + str(res))
