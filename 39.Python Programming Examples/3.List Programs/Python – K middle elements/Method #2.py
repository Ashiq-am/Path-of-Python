# Python3 code to demonstrate working of
# K middle elements
# Using list slicing

# initializing list
test_list = [2, 3, 5, 7, 8, 5, 3, 5, 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# computing strt, and end index
strt_idx = (len(test_list) // 2) - (K // 2)
end_idx = (len(test_list) // 2) + (K // 2)

# slicing extracting middle elements
res = test_list[strt_idx: end_idx + 1]

# printing result
print("Extracted elements list : " + str(res))
