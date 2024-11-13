# Python3 code to demonstrate working of
# Convert Dictionary Value list to Dictionary List
# Using loop

# initializing list
test_list = [{'Gfg': [5, 6, 5]}, {'is': [10, 2, 3]}, {'best': [4, 3, 1]}]

# printing original list
print("The original list is : " + str(test_list))

# Convert Dictionary Value list to Dictionary List
# Using loop
res = [{} for idx in range(len(test_list))]
idx = 0
for sub in test_list:
    for key, val in sub.items():
        for ele in val:
            res[idx][key] = ele
            idx += 1
        idx = 0

# printing result
print("Records after conversion : " + str(res))
