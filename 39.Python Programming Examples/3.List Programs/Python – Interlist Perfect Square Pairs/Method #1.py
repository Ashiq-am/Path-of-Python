# Python3 code to demonstrate
# Interlist Perfect Square Pairs
# using loop

# Initializing lists
test_list1 = [4, 5, 6, 7, 3, 4]
test_list2 = [6, 4, 2, 8, 9, 4]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Flatten List to individual elements
# using chain() + isinstance()
res = []
idx = 0
while (idx < len(test_list1)):
    j = 0
    while (j < len(test_list2)):
        sub = test_list1[idx] * test_list2[j]
        n = sub ** 0.5
        temp = int(n)
        if n == temp:
            res.append((test_list1[idx], test_list2[j]))
        j = j + 1
    idx = idx + 1

# printing result
print("The perfect square pairs are : " + str(res))
