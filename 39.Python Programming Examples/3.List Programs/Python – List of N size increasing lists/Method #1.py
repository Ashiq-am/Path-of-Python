# Python3 code to demonstrate working of
# List of N size increasing lists
# Using loop

# initializing N
N = 2

# initializing M
M = 4

# outer loop manages lists
res = []
for idx in range(1, M):

    # inner loop manages inner elements
    for j in range(idx + 1, M + 1):
        res.append((idx, j))

# printing result
print("The constructed combinations : " + str(res))
