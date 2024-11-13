# Python3 code to demonstrate
# First Even Number in List
# using loop

# Initializing list
test_list = [43, 9, 6, 72, 8, 11]

# printing original list
print("The original list is : " + str(test_list))

# First Even Number in List
# using loop
res = None
for ele in test_list:
    if not ele % 2:
        res = ele
        break

# printing result
print("The first even element in list is : " + str(res))
