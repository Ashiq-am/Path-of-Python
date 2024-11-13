# Python3 code to demonstrate working of
# Elements from list in set
# Using loop

# initializing list
test_list = [5, 6, 2, 3, 2, 6, 5, 8, 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing search set
search_set = {6, 2, 8}

res = []
for ele in test_list:

    # check if element is present in set
    if ele in search_set:
        res.append(ele)

# printing result
print("Set present list elements : " + str(res))
