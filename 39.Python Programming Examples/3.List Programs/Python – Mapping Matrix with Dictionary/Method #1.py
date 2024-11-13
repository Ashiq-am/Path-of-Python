# Python3 code to demonstrate working of
# Mapping Matrix with Dictionary
# Using loop

# initializing list
test_list = [[4, 2, 1], [1, 2, 3], [4, 3, 1]]

# printing original list
print("The original list : " + str(test_list))

# initializing dictionary
sub_dict = {1: "gfg", 2: "best", 3: "CS", 4: "Geeks"}

# Using loop to perform required mapping
res = []
for sub in test_list:
    temp = []
    for ele in sub:
        # mapping values from dictionary
        temp.append(sub_dict[ele])
    res.append(temp)

# printing result
print("Converted Mapped Matrix : " + str(res))
