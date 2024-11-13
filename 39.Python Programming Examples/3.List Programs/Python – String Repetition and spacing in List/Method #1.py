# Python3 code to demonstrate working of
# String Repetition and spacing in List
# Using loop

# initializing list
test_list = ['gfg', 'is', 'best']

# printing original list
print("The original list is : " + str(test_list))

# initializing delim
delim = '-'

# initializing K
K = 3

# String Repetition and spacing in List
# Using loop
res = []
for sub in test_list:
    res.append((sub + delim) * K)

# printing result
print("List after performing operations : " + str(res))
