# Python3 code to demonstrate working of
# Converting string tuples to list tuples
# using list comprehension + eval()

# Initializing list
test_list = ["('gfg', 1)", "('is', 2)", "('best', 3)"]

# printing original list
print("The original list is : " + str(test_list))

# Converting string tuples to list tuples
# using list comprehension + eval()
res = [eval(ele) for ele in test_list]

# printing result
print("The list tuple after conversion : " + str(res))
