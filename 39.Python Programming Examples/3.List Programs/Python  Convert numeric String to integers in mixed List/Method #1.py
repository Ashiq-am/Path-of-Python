# Python3 code to demonstrate working of
# Convert String numbers to integers in mixed List
# using list comprehension + isdigit()

# initialize list
test_list = ["gfg", "1", "is", "6", "best"]

# printing original list
print("The original list : " + str(test_list))

# Convert String numbers to integers in mixed List
# using list comprehension + isdigit()
res = [int(ele) if ele.isdigit() else ele for ele in test_list]

# printing result
print("List after converting string numbers to integers : " + str(res))
