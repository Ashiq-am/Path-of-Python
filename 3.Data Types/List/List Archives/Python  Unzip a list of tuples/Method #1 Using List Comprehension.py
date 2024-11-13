# Python3 code to demonstrate
# Unzip a list of tuples
# using list comprehension

# initializing list of tuples
test_list = [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]

# Printing original list
print("Original list is : " + str(test_list))

# using list comprehension to
# perform Unzipping
res = [[i for i, j in test_list],
       [j for i, j in test_list]]

# Printing modified list
print("Modified list is : " + str(res))
