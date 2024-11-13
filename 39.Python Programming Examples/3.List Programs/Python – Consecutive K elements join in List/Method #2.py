# Python3 code to demonstrate
# Consecutive K elements join in List
# using loop

# Initializing list
test_list = ['g', 'f', 'g', 'i', 's', 'b', 'e', 's', 't']

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 3

# Consecutive K elements join in List
# using loop
res = []
for idx in range(0, len(test_list) - K + 1):
    res.append("".join(test_list[idx: idx + K]))

# printing result
print("List after consecutive joining : " + str(res))
