# Python3 code to demonstrate working of
# Increment Numeric Strings by K
# Using list comprehension + isdigit()

# initializing Matrix
test_list = ["gfg", "234", "is", "98", "123", "best", "4"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 6

# increment Numeric digits.
res = [str(int(ele) + K) if ele.isdigit() else ele for ele in test_list]

# printing result
print("Incremented Numeric Strings : " + str(res))
