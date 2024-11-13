# Python3 code to demonstrate working of
# Similar all elements as List in Matrix rows
# Using loop

# initializing Matrix
test_list = [[1, 1, 1], [4, 4],
             [3, 3, 3], [5, 5, 5, 5]]

# printing original list
print("The original list is : " + str(test_list))

# initializing tar_list
tar_list = [1, 4, 3, 5]

res = True
flag = 0
for idx in range(len(test_list)):
    for ele in test_list[idx]:

        # checking for row index
        # equal to list index elements
        if ele != tar_list[idx]:
            res = False
            flag = 1
            break

    if flag:
        break

# printing result
print("Are row index element similar\
	to list index element ? : " + str(res))
