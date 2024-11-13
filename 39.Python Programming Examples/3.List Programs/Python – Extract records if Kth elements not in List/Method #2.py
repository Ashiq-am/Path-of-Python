# Python3 code to demonstrate working of
# Extract records if Kth elements not in List
# Using list comprehension + set()

# initializing list
test_list = [(5, 3), (7, 4), (1, 3), (7, 8), (0, 6)]

# printing original list
print("The original list : " + str(test_list))

# initializing arg. list
arg_list = [4, 8, 4]

# initializing K
K = 1

# Compiling set() and conditionals into single comprehension
res = [(key, val) for key, val in test_list if val not in set(arg_list)]

# printing result
print("Extracted elements : " + str(res))
