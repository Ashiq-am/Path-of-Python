# Python3 code to demonstrate working of
# Construct tuple from string and list
# using list conversion to tuple + tuple()

# initialize list and string
test_list = ["gfg", "is"]
test_str = "best"

# printing original list and tuple
print("The original list : " + str(test_list))
print("The original string : " + test_str)

# Construct tuple from string and list
# using list conversion to tuple + tuple()
res = tuple(test_list + [test_str])

# printing result
print("The aggregated tuple is : " + str(res))
