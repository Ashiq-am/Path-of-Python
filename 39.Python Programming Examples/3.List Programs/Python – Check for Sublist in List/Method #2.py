# Python3 code to demonstrate working of
# Check for Sublist in List
# Using any() + list slicing + generator expression

# initializing list
test_list = [5, 6, 3, 8, 2, 1, 7, 1]

# printing original list
print("The original list : " + str(test_list))

# initializing sublist
sublist = [8, 2, 1]

# Check for Sublist in List
# Using any() + list slicing + generator expression
res = any(test_list[idx: idx + len(sublist)] == sublist
          for idx in range(len(test_list) - len(sublist) + 1))

# printing result
print("Is sublist present in list ? : " + str(res))
