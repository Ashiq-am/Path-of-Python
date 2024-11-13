# Python3 code to demonstrate working of
# Segregate True and False value indices
# using loop + enumerate()

# initialize list
test_list = [False, True, False, False, True, True]

# printing original list
print("The original list is : " + str(test_list))

# Segregate True and False value indices
# using loop + enumerate()
res_true, res_false = [], []
for i, ele in enumerate(test_list):
	temp = res_true if ele else res_false
	temp.append(i)

# printing result
print("True indices after grouping : " + str(res_true))
print("False indices after grouping : " + str(res_false))
