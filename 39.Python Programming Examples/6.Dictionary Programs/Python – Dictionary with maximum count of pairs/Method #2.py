# Python3 code to demonstrate working of
# Dictionary with maximum keys
# Using max() + key = len

# initializing list
test_list = [{"gfg": 2, "best": 4},
             {"gfg": 2, "is": 3, "best": 4},
             {"gfg": 2}]

# printing original list
print("The original list is : " + str(test_list))

# maximum length dict using len param
res = max(test_list, key=len)

# printing results
print("Maximum keys Dictionary : " + str(res))
