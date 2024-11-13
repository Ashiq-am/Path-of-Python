# Python3 code to demonstrate working of
# Cross Join every Kth segment
# Using yield + loop

# helper function
def pair_merge(test_list1, test_list2, K):
    idx1 = 0
    idx2 = 0
    while (idx1 < len(test_list1)):

        # get K segments
        for i in range(K):
            yield test_list1[idx1]
            idx1 += 1
        for i in range(K):
            yield test_list2[idx2]
            idx2 += 1


# initializing lists
test_list1 = [4, 3, 8, 2, 6, 7]
test_list2 = [5, 6, 7, 4, 3, 1]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# initializing K
K = 2

# calling helper func. in generator expression
res = [ele for ele in pair_merge(test_list1, test_list2, K)]

# printing result
print("The cross joined list : " + str(res))
