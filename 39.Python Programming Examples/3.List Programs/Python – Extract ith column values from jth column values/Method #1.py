# Python3 code to demonstrate working of
# Extract ith column values from jth column values
# Using loop

# initializing list
test_list = [[4, 5, 6], [2, 5, 7], [9, 8, 2], [10, 2, 6]]

# printing original list
print("The original list is : " + str(test_list))

# initializing list
search_list = [5, 2]

# initializing search index
search_idx = 1

# initializing extract index
ext_idx = 2

# Extract ith column values from jth column values
# Using loop
res = []
for sub in test_list:
    if sub[search_idx] in search_list:
        res.append(sub[ext_idx])

# printing result
print("The extracted elements : " + str(res))
