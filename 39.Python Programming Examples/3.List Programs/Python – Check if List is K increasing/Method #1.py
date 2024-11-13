# Python3 code to demonstrate working of
# Check if List is K increasing
# Using loop

# initializing list
test_list = [4, 7, 10, 13, 16, 19]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

res = True
for idx in range(len(test_list) - 1):

    # flagging if not found
    if test_list[idx + 1] != test_list[idx] + K:
        res = False

# printing results
print("Is list K increasing ? : " + str(res))
