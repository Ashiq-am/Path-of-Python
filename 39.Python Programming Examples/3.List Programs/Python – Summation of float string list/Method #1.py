# Python3 code to demonstrate working of
# Summation of float string list
# using sum() + float() + generator

# initialize lists
test_list = ['4.5', '7.8', '9.8', '10.3']

# printing original list
print("The original list is : " + str(test_list))

# Summation of float string list
# using sum() + float() + generator
res_sum = sum(float(sub) for sub in test_list)

# printing result
print("The summation of float string list : " + str(res_sum))
