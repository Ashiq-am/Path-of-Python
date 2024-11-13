# Python3 code to demonstrate working of
# Similar other index element if K
# Using list comprehension + enumerate()

# initializing list
test_list = [5, 7, 3, 2, 3, 8, 6]

# printing original list
print("The original list : " + str(test_list))

# initializing arg. list
arg_list = [4, 5, 8, 3, 7, 9, 3]

# initializing K
K = 3

# Using enumerate() to locate similar index in other list and extract element
res = [ele for idx, ele in enumerate(arg_list) if test_list[idx] == K]

# printing result
print("Extracted elements : " + str(res))
