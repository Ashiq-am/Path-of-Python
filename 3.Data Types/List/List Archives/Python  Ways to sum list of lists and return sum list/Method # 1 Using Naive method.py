# Python code to demonstrate
# sum of list of list
# using naive method

# Declaring initial list of list
L = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# Printing list of list
print("Initial List - ", str(L))

# Using naive method
res = list()
for j in range(0, len(L[0])):
    tmp = 0
    for i in range(0, len(L)):
        tmp = tmp + L[i][j]
    res.append(tmp)

# printing result
print("final list - ", str(res))
