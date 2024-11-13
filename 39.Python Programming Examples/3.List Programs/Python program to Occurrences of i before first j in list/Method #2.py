# Python3 code to demonstrate working of
# Occurrences of i before first j
# Using index() + slicing + count()

# initializing Matrix
test_list = [4, 5, 6, 4, 1, 4, 8, 5, 4, 3, 4, 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing i, j
i, j = 4, 8

# getting index
jidx = test_list.index(j)

# slicing list
temp = test_list[:jidx]

# getting count
res = temp.count(i)

# printing result
print("Number of i's till 1st j : " + str(res))
