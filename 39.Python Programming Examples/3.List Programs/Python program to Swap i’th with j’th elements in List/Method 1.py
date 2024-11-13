# Python3 code to demonstrate working of
# Toggle i,j elements in List
# Using loop + conditional statements

# initializing list
test_list = [4, 7, 8, 0, 8, 4, 2, 9, 4, 8, 4]

# printing original list
print("The original list is : " + str(test_list))

# initializing i, j
i, j = 4, 8

for idx in range(len(test_list)):

    # perform toggling
    if int(test_list[idx]) == i:
        test_list[idx] = j
    elif int(test_list[idx]) == j:
        test_list[idx] = i

# printing result
print("The altered list : " + str(test_list))
