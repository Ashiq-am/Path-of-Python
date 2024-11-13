# Python3 code to demonstrate working of
# Convert list to Single Dictionary Key Value list
# Using loop

# initializing list
test_list = [5, 6, 3, 8, 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# Convert list to Single Dictionary Key Value list
# Using loop
res = {test_list[K] : test_list[:K] + test_list[K + 1:]}

# printing result
print("Records after conversion : " + str(res))
