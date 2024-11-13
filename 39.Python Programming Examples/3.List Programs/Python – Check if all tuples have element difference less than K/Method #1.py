# Python3 code to demonstrate working of
# Check if all tuples have element difference less than K
# Using loop

# initializing list
test_list = [(3, 4), (1, 2), (7, 8), (9, 8)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

res = True
for ele1, ele2 in test_list:

    # using abs() to compute absolute difference
    if abs(ele1 - ele2) >= K:
        res = False

# printing result
print("Are all elements difference less than K ? : " + str(res))
