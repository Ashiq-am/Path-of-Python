# Python3 code to demonstrate working of
# First K unique elements
# Using loop

# initializing list
test_list = [6, 7, 6, 7, 8, 3, 9, 11]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

# First K unique elements
# Using loop
store = []
res = []
cnt = 0
for ele in test_list:
    if ele not in store:
        cnt = cnt + 1
        store.append(ele)
    res.append(ele)
    if cnt >= K:
        break

# printing result
print("The extracted elements : " + str(res))
