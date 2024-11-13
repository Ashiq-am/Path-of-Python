# Python3 code to demonstrate working of
# Test for alternate peak List
# Using loop

# initializing list
test_list = [2, 4, 1, 6, 4, 8, 0]

# printing original list
print("The original list is : " + str(test_list))

res = True
for idx in range(1, len(test_list) - 1):

    # breaking if not alternate peaks
    if not ((test_list[idx - 1] < test_list[idx]
             and test_list[idx + 1] < test_list[idx])
            or (test_list[idx - 1] > test_list[idx]
                and test_list[idx + 1] > test_list[idx])):
        res = False

# printing result
print("Is list forming alternate peaks ? : " + str(res))
