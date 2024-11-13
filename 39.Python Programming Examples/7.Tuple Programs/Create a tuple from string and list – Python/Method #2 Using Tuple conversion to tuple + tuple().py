# Python3 code to demonstrate working of
# Construct tuple from string and list
# using tuple conversion to tuple + tuple()

# initialize list and string
test_list = ["is", "best"]
test_str = "gfg"

# printing original list and tuple
print("The original list : " + str(test_list))
print("The original string : " + test_str)

# Construct tuple from string and list
# using tuple conversion to tuple + tuple()
res = (test_str, ) + tuple(test_list)

# printing result
print("The aggregated tuple is : " + str(res))
