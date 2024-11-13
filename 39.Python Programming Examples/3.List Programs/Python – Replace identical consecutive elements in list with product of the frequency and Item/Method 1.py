# Python3 code to demonstrate working of
# Equal Consecution Product
# Using loop

# initializing list
test_list = [3, 3, 3, 3, 6, 7, 5, 5, 5, 8,
             8, 6, 6, 6, 6, 6, 1, 1, 1, 2, 2]

# printing original list
print("The original list is : " + str(test_list))

res = []
count = 1
for idx in range(1, len(test_list)):

    # checking with prev element
    if test_list[idx - 1] != test_list[idx]:
        # appending product
        res.append((test_list[idx - 1] * count))
        count = 0
    count += 1
res.append((test_list[-1] * count))

# printing result
print("Elements after equal Consecution product : " + str(res))
