# Python3 code to demonstrate
# Incremental and Cyclic Repetition of List Elements
# using loop + enumerate()

# Initializing list
test_list = ['g', 'f', 'g', 'C', 'S']

# printing original list
print("The original list is : " + str(test_list))

# Initializing range
i, j = 2, 4

# Incremental and Cyclic Repetition of List Elements
# using loop + enumerate()
res = []
temp = list(range(i, j + 1))
for idx, ele in enumerate(test_list):
    res.append(ele * temp[idx % len(temp)])

# printing result
print("Repetition List is : " + str(res))
