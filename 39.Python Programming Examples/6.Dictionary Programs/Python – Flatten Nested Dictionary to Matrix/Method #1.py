# Python3 code to demonstrate working of
# Flatten Nested Dictionary to Matrix
# using zip() + loop + map()

# initializing dictionary
test_dict = {'Gfg1': {'CS': 1, 'GATE': 2},
             'Gfg2': {'CS': 2, 'GATE': 3},
             'Gfg3': {'CS': 4, 'GATE': 5}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Flatten Nested Dictionary to Matrix
# using zip() + loop + map()
temp = list(test_dict.values())
sub = set()
for ele in temp:
    for idx in ele:
        sub.add(idx)
res = []
res.append(sub)
for key, val in test_dict.items():
    temp2 = []
    for idx in sub:
        temp2.append(val.get(idx, 0))
    res.append(temp2)

res = [[idx for idx, val in test_dict.items()]] + list(map(list, zip(*res)))

# printing result
print("The Grouped dictionary list is : " + str(res))
