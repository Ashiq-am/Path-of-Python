# initializing list
test_list = [[3], [1, 7], [10, 2, 4], [8, 6, 5, 1, 4]]

# printing original list
print("The original list is : " + str(test_list))

res = True
for idx in range(len(test_list) - 1):

    # flag off in case next length is not greater
    # than current
    if len(test_list[idx + 1]) <= len(test_list[idx]):
        res = False
        break

# printing result
print("Are rows of increasing lengths ? : " + str(res))
