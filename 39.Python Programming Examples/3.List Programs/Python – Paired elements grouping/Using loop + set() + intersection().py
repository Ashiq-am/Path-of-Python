# Python3 code to demonstrate working of
# Paired elements grouping
# Using loop + set() + intersection()

# initializing list
test_list = [(1, 3), (4, 5), (1, 7), (3, 4), (7, 8)]

# printing original list
print("The original list is : " + str(test_list))

# Paired elements grouping
# Using loop + set() + intersection()
res = []
for sub in test_list:
    idx = test_list.index(sub)
    sub_list = test_list[idx + 1:]
    if idx <= len(test_list) - 2:
        for ele in sub_list:
            intrsct = set(sub).intersection(set(ele))
            if len(intrsct) > 0:
                res.append(set(sub + ele))

# printing result
print("The grouped list : " + str(res))
