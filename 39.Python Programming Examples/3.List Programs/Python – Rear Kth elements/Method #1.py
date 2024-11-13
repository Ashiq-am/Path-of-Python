# Python3 code to demonstrate working of
# Rear Kth elements
# Using loop

# initializing list
test_list = [3, 5, 7, 9, 10, 2, 8, 6]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# Rear Kth elements
res = []
test_list.reverse()
for idx, ele in enumerate(test_list):

    # Extracting elements divisible by K
    if idx % K == 0:
        res.append(ele)

# printing result
print("Rear Kth elements : " + str(res))
