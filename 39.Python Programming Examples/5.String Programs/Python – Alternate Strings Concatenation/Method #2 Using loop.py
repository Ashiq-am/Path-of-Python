# Python3 code to demonstrate
# Alternate Strings Concatenation
# using loop

# initializing list
test_list = ["GFG", "is", " for", " Computer", " Science", " learning"]

# printing original list
print("The original list : " + str(test_list))

# using loop
# Alternate Strings Concatenation
res = ["", ""]
for i in range(0, len(test_list)):
	if(i % 2):
		res[1] += test_list[i]
	else :
		res[0] += test_list[i]

# print result
print("The alternate elements concatenation list : " + str(res))
