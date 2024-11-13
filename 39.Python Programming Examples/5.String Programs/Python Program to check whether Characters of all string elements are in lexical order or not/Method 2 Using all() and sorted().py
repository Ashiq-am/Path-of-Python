# initializing list
test_list = ["dent", "flop", "most", "cent"]

# printing original list
print("The original list is : " + str(test_list))

# using all() to check all elements to be sorted
res = all(ele == ''.join(sorted(ele)) for ele in test_list)

# printing result
print("Are all strings ordered ? : " + str(res))
