# Python3 code to demonstrate working of
# Extract Key's value from Mixed Dictionaries List
# Using update() + loop

# initializing list
test_list = [{"Gfg": 3, "b": 7},
             {"is": 5, 'a': 10},
             {"Best": 9, 'c': 11}]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 'Best'

res = dict()
for sub in test_list:
    # merging all Dictionaries into 1
    res.update(sub)

# printing result
print("The extracted value : " + str(res[K]))
