# Python3 code to demonstrate working of
# Segregate True and False value indices
# using loops

# initialize list
test_list = [False, True, False, False, True, True]

# printing original list
print("The original list is : " + str(test_list))

# Segregate True and False value indices
# using loops
res_true, res_false = [], []
for i in range(0, len(test_list)):
	if test_list[i]:
		res_true.append(i)
	else :
		res_false.append(i)

# printing result
print("True indices after grouping : " + str(res_true))
print("False indices after grouping : " + str(res_false))
