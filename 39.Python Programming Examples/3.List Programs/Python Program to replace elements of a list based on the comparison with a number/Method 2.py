# initializing list
test_list = [7, 4, 3, 2, 6, 8, 9, 1]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# initializing low and high Replacement Replacement
low, high = 2, 9

# list comprehension for shorthand solution
res = [high if ele > K else low for ele in test_list]

# printing result
print("List after replacement ? : " + str(res))
