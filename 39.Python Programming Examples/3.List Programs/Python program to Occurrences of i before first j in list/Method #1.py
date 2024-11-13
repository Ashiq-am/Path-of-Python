# Python3 code to demonstrate working of
# Occurrences of i before first j
# Using loop

# initializing Matrix
test_list = [4, 5, 6, 4, 1, 4, 8, 5, 4, 3, 4, 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing i, j
i, j = 4, 8

res = 0
for ele in test_list:

    # breaking on 1st j
    if ele == j:
        break

    # counting i till 1st j
    if ele == i:
        res += 1

# printing result
print("Number of i's till 1st j : " + str(res))
