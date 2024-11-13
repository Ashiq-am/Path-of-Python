# initializing list
test_list = [4, 6, 7, 3, 1, 9, 2, 19]

# printing original list
print("The original list is : " + str(test_list))

# initializing index list
idx_list = [3, 1, 4, 6]

res = []
for idx, ele in enumerate(test_list):
    if idx in idx_list:

        # incase of repetition
        res.extend([ele, ele])
    else:
        res.append(ele)

# printing result
print("The Custom elements repetition : " + str(res))
