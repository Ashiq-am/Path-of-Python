# Python3 code to demonstrate working of
# Min / Max value in float string list
# using min()/max() + float() + generator

# initialize lists
test_list = ['4.5', '7.8', '9.8', '10.3']

# printing original list
print("The original list is : " + str(test_list))

# Min / Max value in float string list
# using min()/max() +float + lambda function
res_min = min(test_list,key=lambda x:float(x))
res_max = max(test_list,key=lambda x:float(x))

# printing result
print("The min value of list : " + str(res_min))
print("The max value of list : " + str(res_max))
