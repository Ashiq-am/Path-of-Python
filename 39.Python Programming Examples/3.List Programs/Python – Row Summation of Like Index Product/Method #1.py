# Python3 code to demonstrate working of
# Row Summation of Like Index Product
# Using loop

# initializing list
test_list = [[3, 4, 5], [1, 7, 5], [8, 1, 2]]

# printing original list
print("The original list is : " + str(test_list))

# initializing mul list
mul_list = [5, 2, 3]

# Using loop
res = []
for sub in test_list:
    sum = 0
    for idx, ele in enumerate(sub):
        # performing summation of product with list elements
        sum = sum + (ele * mul_list[idx])

    # adding each row sum
    res.append(sum)

# printing result
print("List after multiplication : " + str(res))
