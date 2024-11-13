from collections import defaultdict

# initializing list
test_list = ["gfg", "is", "best", "good"]

# printing original list
print("The original list is : " + str(test_list))

# initializing values list
val_list = [1, 4, 5, 6, 7, 8, 8, 5, 4]

# initializing K
K = 2

# work list
val_list = val_list[:(len(test_list) * K)]

# gets requried dictionary list
res = defaultdict(list)
key_cnt = 0
for idx in range(0, len(val_list)):

    # append values to required keys
    res[test_list[key_cnt]].append(val_list[idx])

    # increment keys when K
    if (idx + 1) % K == 0:
        key_cnt += 1

# printing result
print("The constructed dictionary : " + str(dict(res)))
