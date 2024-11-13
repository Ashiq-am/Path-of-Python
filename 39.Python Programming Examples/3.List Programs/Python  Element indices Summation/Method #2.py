# Python code to demonstrate
# Element indices Summation
# using list comprehension + sum()

# initializing list
test_list = [1, 3, 4, 3, 6, 7]

# printing initial list
print ("Original list : " + str(test_list))

# using list comprehension + sum()
# Element indices Summation
# to find indices for 3
res_list = [i for i in range(len(test_list)) if test_list[i] == 3]
res = sum(res_list)

# printing resultant list
print ("New indices summation : " + str(res))
