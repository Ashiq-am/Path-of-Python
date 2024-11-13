# Python3 code to demonstrate working of
# Maximum of K element in other list
# Using loop + max()

# initializing lists
test_list1 = [4, 3, 6, 2, 9]
test_list2 = [3, 6, 3, 4, 3]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# initializing K
K = 3

res = []
for idx in range(len(test_list1)):

    # checking for K in 2nd list
    if test_list2[idx] == K:
        res.append(test_list1[idx])

# getting Maximum element
res = max(res)

# printing result
print("Extracted Maximum element : " + str(res))
