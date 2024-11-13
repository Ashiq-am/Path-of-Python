# Python3 code to demonstrate working of
# Segregate elements by delimiter
# Using list comprehension + split()

# initializing list
test_list = ["7$2", "8$5", "9$1", "8$10", "32$6"]

# printing original list
print("The original list : " + str(test_list))

# using delim
delim = "$"

# using split() to split and different list comprehension
# assigns results to different lists
res1, res2 = [ele.split(delim)[0] for ele in test_list], [ele.split(delim)[1] for ele in test_list]

# printing result
print("The filtered list 1 : " + str(res1))
print("The filtered list 2 : " + str(res2))
