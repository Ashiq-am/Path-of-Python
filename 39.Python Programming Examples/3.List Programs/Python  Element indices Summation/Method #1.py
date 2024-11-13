# Python code to demonstrate
# Element indices Summation
# using naive method + sum()

# initializing list
test_list = [1, 3, 4, 3, 6, 7]

# printing initial list
print ("Original list : " + str(test_list))

# using naive method
# Element indices Summation
# to find indices for 3
res_list = []
for i in range(0, len(test_list)) :
	if test_list[i] == 3 :
		res_list.append(i)
res = sum(res_list)

# printing resultant list
print ("New indices summation : " + str(res))
