# Python3 code to demonstrate working of
# Extract Kth element of every Nth tuple in List
# Using loop

# initializing list
test_list = [(4, 5, 3), (3, 4, 7), (4, 3, 2), (4, 7, 8),
             (6, 4, 7), (2, 5, 7), (1, 9, 10), (3, 5, 7)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 1

# initializing N
N = 3

res = []
for idx in range(0, len(test_list), N):
    # extract Kth element
    res.append(test_list[idx][K])

# printing result
print("The extracted elements : " + str(res))
