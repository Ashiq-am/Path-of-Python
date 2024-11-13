# Python3 code to demonstrate working of
# List Elements Grouping in Matrix
# Using loop

# initializing list
test_list = [[4, 6], [1, 2], [2, 6], [7, 8], [1, 4]]

# printing original list
print("The original list is : " + str(test_list))

# initializing check_list
check_list = [1, 2, 4, 6]

res = []
while test_list:

    # getting row
    sub1 = test_list.pop()

    # getting elements not in row
    sub2 = [ele for ele in check_list if ele not in sub1]
    try:

        # testing if we have list of removed elements
        test_list.remove(sub2)

        # grouping if present
        res.append([sub1, sub2])
    except ValueError:

        # ungrouped.
        res.append(sub1)

# printing result
print("The Grouped rows : " + str(res))
