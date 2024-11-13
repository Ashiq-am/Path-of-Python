# Python3 code to demonstrate working of
# Rearrange elements second index greater than first
# Using loop

# initializing lists
test_list1 = [14, 16, 18, 110]
test_list2 = [13, 15, 17, 19, 111]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Rearrange elements second index greater than first
# Using loop
x = y = 0
res1, res2 = [], []
while x < len(test_list2) and y < len(test_list1):

    # checking for greater element
    if test_list2[x] > test_list1[y]:
        res2.append(test_list2[x])
        res1.append(test_list1[y])
        while y < len(test_list1) and test_list2[x] > test_list1[y]:
            res1[-1] = test_list1[y]
            y += 1
    x += 1

# printing result
print("List 2 after conversion : " + str(res2))
