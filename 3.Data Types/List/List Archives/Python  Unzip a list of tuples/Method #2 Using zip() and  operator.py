# Python3 code to demonstrate
# Unzip a list of tuples
# using zip() and * operator

# initializing list of tuples
test_list = [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]

# Printing original list
print("Original list is : " + str(test_list))

# using zip() and * operator to
# perform Unzipping
res = list(zip(*test_list))

# Printing modified list
print("Modified list is : " + str(res))
