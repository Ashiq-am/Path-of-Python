# Python3 code to demonstrate
# Consecutive K elements join in List
# using List comprehension

# Initializing list
test_list = ['g', 'f', 'g', 'i', 's', 'b', 'e', 's', 't']

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 3

# Consecutive K elements join in List
# using List comprehension
res = ["".join(test_list[idx: idx + K]) for idx in range(len(test_list) - K + 1)]

# printing result
print("List after consecutive joining : " + str(res))
