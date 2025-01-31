# Python3 code to demonstrate
# Prefix extraction depending on size
# using loop

# Initializing list
test_list = ['geeksforgeeks', 'is', 'best', 'for', 'geeks']

# Initializing K
K = 2

# Initializing N
N = 4

# printing original list
print("The original list is : " + str(test_list))

# Prefix extraction depending on size
# using loop
res = []
for idx in test_list:
    if len(idx) >= N:
        res.append(idx[:K])

# printing result
print("List after prefix extraction : " + str(res))
