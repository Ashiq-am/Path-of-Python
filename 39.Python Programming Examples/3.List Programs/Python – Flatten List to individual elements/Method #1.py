# Python3 code to demonstrate
# Flatten List to individual elements
# using loop + isinstance()

def flatten(test_list):
    if isinstance(test_list, list):
        temp = []
        for ele in test_list:
            temp.extend(flatten(ele))
        return temp
    else:
        return [test_list]


# Initializing list
test_list = ['gfg', 1, [5, 6, 'geeks'], 67.4, [5], 'best']

# printing original list
print("The original list is : " + str(test_list))

# Flatten List to individual elements
# using loop + isinstance()
res = flatten(test_list)

# printing result
print("The List after flattening : " + str(res))
