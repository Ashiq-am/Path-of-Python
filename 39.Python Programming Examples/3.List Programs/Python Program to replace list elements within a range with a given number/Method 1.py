# initializing list
test_list = [4, 6, 8, 1, 2, 9, 0, 10, 12, 3, 9, 1]

# printing original list
print("The original list is : " + str(test_list))

# initializing i, j
i, j = 4, 8

# initializing K
K = 9

# getting range using slicing and
# required elements using * operator
test_list[i:j] = [K] * (j - i)

# printing result
print("Range Updated list : " + str(test_list))
